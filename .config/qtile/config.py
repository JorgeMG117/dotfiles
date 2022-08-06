from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Theme
from os import path
import json
theme = "/home/jorge/.config/qtile/themes/dracula.json"

if not path.isfile(theme):
    raise Exception(f'"{theme}" does not exist')
with open(path.join(theme)) as f:
    colors = json.load(f)


mod = "mod4"
terminal = guess_terminal()

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Switch focus of monitors
    #([mod], "period", lazy.next_screen()),
    #([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun -show-icons")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal File Explorer
    ([mod], "f", lazy.spawn("alacritty -e ranger")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot '%Y-%m-%d_%H:%M:%S_$wx$h.png' -e 'mv $f ~/screenshots/'")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]

groups = [Group(i) for i in [
    "   ","   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend(
        [
            Key(
                [mod],
                actual_key,
                lazy.group[group.name].toscreen()),

            Key(
                [mod, "shift"],
                actual_key,
                lazy.window.togroup(group.name),
            ),
        ]
    )

layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 4
}

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    layout.MonadTall(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()

base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

powerline = lambda fg='light', bg='dark': widget.TextBox(
    **base(fg, bg),
    text="",
    fontsize=37,
    padding=-3
)

screens = [
    Screen(
        bottom=bar.Bar(
            [
                separator(),
                widget.GroupBox(
                    **base(fg='light'),
                    font='agave Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=colors['active'],
                    inactive=colors['inactive'],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=colors['urgent'],
                    this_current_screen_border=colors['focus'],
                    this_screen_border=colors['grey'],
                    other_current_screen_border=colors['dark'],
                    other_screen_border=colors['dark'],
                    disable_drag=True
                ),
                separator(),
                widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
                separator(),

                powerline('color4', 'dark'),
                widget.Battery(
                    **base(bg='color4'),
                    charge_char=' ',
                    discharge_char=' ',
                    format='{char} {percent:2.0%} ',
                    low_percentage = 0.3
                ),
                powerline('color3', 'color4'),
                #icon(bg='color3', text=' '),
                widget.Net(**base(bg='color3'), interface='wlp2s0'),
                powerline('color2', 'color3'),
                widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
                widget.CurrentLayout(**base(bg='color2'), padding=5),
                powerline('color1', 'color2'),
                widget.Clock(**base(bg='color1'), format="%d/%m/%Y - %H:%M"),
                #widget.QuickExit(),
                powerline('dark', 'color1'),
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
wmname = "LG3D"