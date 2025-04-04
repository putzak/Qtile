# cOpyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
# from libqtile.config import EzKey as Key
import os
import subprocess
from qtile_extras import widget

from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.window.toggle_floating()),
    #Custom Keys
    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([], "XF86ScreenSaver", lazy.spawn("zsh -c ~/.screentoggle.sh")),
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([mod], 'z', lazy.group['0'].dropdown_toggle('remmina')),
    Key([mod], 'b', lazy.group['0'].dropdown_toggle('status')),
    Key([mod], 'v', lazy.group['0'].dropdown_toggle('term')),
    Key([mod], 'n', lazy.group['0'].dropdown_toggle('bluetooth')),
    Key([mod], 'm', lazy.group['0'].dropdown_toggle('pavu')),
    Key([mod], 'c', lazy.group['0'].dropdown_toggle('ranger')),
    Key([mod], 'x', lazy.group['0'].dropdown_toggle('ncdu')),
#    Key([mod], 'z', lazy.group['0'].dropdown_toggle('ticker')),
]

# groups = [Group(i) for i in "bti123456789"]
groups = [ 
    ScratchPad('0', [
        DropDown(
            'remmina',
            "alacritty -e flatpak run --user org.remmina.Remmina",
            height = 0.9,
            width = 0.9,
            x = 0.05,
            y = 0.05,
            on_focus_lost_hide = False,
            warp_pointer = False,
            ),
        DropDown(
            'ticker',
            "alacritty -e ticker -w LUNR,OCGN,GRT6719-USD,AM.PA,RHM.DE,LMT,NOC,DRS,ICU --show-fundamentals",
            height = 0.9,
            width = 0.9,
            x = 0.05,
            y = 0.05,
            on_focus_lost_hide = False,
            opacity = 0.95,
            warp_pointer = False,
            ),
        DropDown(
            'ncdu',
            "alacritty -e ncdu",
            height = 0.9,
            width = 0.9,
            x = 0.05,
            y = 0.05,
            on_focus_lost_hide = False,
            opacity = 0.95,
            warp_pointer = False,
            ),
        DropDown(
            'ranger',
            "alacritty -e sudo ranger",
            height = 0.9,
            width = 0.9,
            x = 0.05,
            y = 0.05,
            on_focus_lost_hide = False,
            opacity = 0.95,
            warp_pointer = False,
            ),
        DropDown(
            'status',
            "alacritty -e bpytop",
            height = 0.9,
            width = 0.9,
            x = 0.05,
            y = 0.05,
            on_focus_lost_hide = False,
            opacity = 0.95,
            warp_pointer = False,
            ),
        DropDown(
            'pavu',
            "pavucontrol",
            height = 0.9,
            width = 0.9,
            x = 0.05,
            y = 0.05,
            on_focus_lost_hide = False,
            opacity = 0.95,
            warp_pointer = False,
            ),
        DropDown(
            'bluetooth',
            "alacritty -e bluetoothctl",
            height = 0.9,
            width = 0.9,
            x = 0.05,
            y = 0.05,
            on_focus_lost_hide = False,
            opacity = 0.95,
            warp_pointer = False,
            ),
        DropDown(
            'term',
            "alacritty",
            height = 0.9,
            width = 0.9,
            x = 0.05,
            y = 0.05,
            on_focus_lost_hide = False,
            opacity = 0.95,
            warp_pointer = False,
            ),
]),
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
    Group("9"),
    Group("t", label="T"), 
    Group("i", label="I"), 
    Group("g", label="G"),
    Group("d", label="D"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack="#0C3B71",
        border_focus="#0C3B71", 
        border_normal="#181818",
        border_width=4, 
        margin=2, 
        margin_on_single=0),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Roboto",
    fontsize=15,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.WindowCount(
                    background='#0C3B71', 
                    ),
                widget.CurrentLayout(
                    background="#0C3B71",
                    foreground="#D8F3CD"
                    ),
                widget.TextBox(' '),
                widget.GroupBox(
                    highlight_method='text', 
                    hide_unused=True
                    ),
                #widget.TextBox(
                #    "|", 
                #    foreground="#0C3B71", 
                #    fontsize="35"
                #    ),
                widget.Prompt(foreground="#d75f5f"),
                widget.TextBox(' '),
                widget.WindowName(
                    ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),                
                widget.TextBox(
                    "MEM%",
                    ),
                widget.GenPollCommand(
                    cmd="~/Scripts/memory.sh",
                    update_interval=3,
                    shell = True,
                    foreground='#0C3B71',
                    ),
                widget.TextBox(
                    "USR%",
                    ),
                widget.GenPollCommand(
                    cmd="mpstat | awk 'FNR == 4 {print $3}'",
                    update_interval=3,
                    shell = True,
                    foreground='#0C3B71',
                    ),
                widget.TextBox(
                    "SYS%",
                    ),
                widget.GenPollCommand(
                    cmd="mpstat | awk 'FNR == 4 {print $5}'",
                    update_interval=3,
                    shell = True,
                    foreground='#0C3B71', 
                    ),
                widget.TextBox(
                    "PROC#",
                    ),
                widget.GenPollCommand(
                    cmd="pidstat | wc -l",
                    update_interval=3,
                    shell = True,
                    foreground='#0C3B71',               
                    ),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(
                    timezone="Europe/Amsterdam",
                    format="%d-%m %H:%M", 
                    ),
                widget.WiFiIcon(foreground="#D8F3CD"),   
                widget.UPowerWidget(border_colour="#666666", border_charge_colour="#D8F3CD"),
                # widget.Wlan(),
                # widget.QuickExit(foreground="#d75f5f"),
                # widget.Battery(
                #    discharge_char='-', 
                #    charge_char='+', 
                #    format='{char} {percent:2.0%}', 
                #    # low_percentage='0.9', 
                #    # low_foreground='#FF0000', 
                #    ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
