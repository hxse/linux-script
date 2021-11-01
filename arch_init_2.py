import subprocess

text=input('添加清华镜像,按回车继续,任意键跳过')
if not text:
    with open('/etc/pacman.d/mirrorlist', 'w',encoding='utf8')as f:
        f.write('Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch')
    print('清华镜像已添加到/etc/pacman.d/mirrorlist, 请用 sudo pacman -Syy更新包缓存')
    subprocess.run(['pacman', '-Syy'])

text=input('安装中文字体,按回车继续')
if not text:
	subprocess.run(['pacman', '-S','noto-fonts'])
	subprocess.run(['pacman', '-S','noto-fonts-cjk'])
	subprocess.run(['pacman', '-S','noto-fonts-emoji'])

text=input('添加git代理,按回车继续')
if not text:
	subprocess.run(['git', 'config','--global','http.proxy','http://127.0.0.1:7890'])
	subprocess.run(['git', 'config','--global','https.proxy','http://127.0.0.1:7890'])

text=input('add proxychains4')
if not text:
	subprocess.run(['pacman', '-S','proxychains4'])
	subprocess.run(['echo', 'http 127.0.0.1 7890','>>','/etc/proxychains.conf'])
	subprocess.run(['echo', 'socks5 127.0.0.1 7891','>>','/etc/proxychains.conf'])


text=input('安装fcitx5,按回车继续')
if not text:
	subprocess.run(['pacman', '-S','fcitx5-im','fcitx5-configtool'])
    text='''GTK_IM_MODULE DEFAULT=fcitx
QT_IM_MODULE  DEFAULT=fcitx
XMODIFIERS    DEFAULT=@im=fcitx
INPUT_METHOD  DEFAULT=fcitx
SDL_IM_MODULE DEFAULT=fcitx
'''
	subprocess.run(['echo', text,'>>','~/.pam_environment'])

text=input('reboot enabling environment variables?')
if not text:
    subprocess.run(['reboot'])
    
text=input('安装xorg,按回车继续')
if not text:
	subprocess.run(['pacman', '-S','xorg','xorg-xinit'])

text=input('安装i3,按回车继续')
if not text:
	subprocess.run(['pacman', '-S','i3'])
	subprocess.run(['pacman', '-S','st'])
	subprocess.run(['pacman', '-S','dmenu'])
    
text=input('add i3 to xinitrc and startx')
if not text:
	subprocess.run(['echo', 'exec i3','>>','~/.xinitrc'])
	subprocess.run(['echo', 'exec fcitx5','>>','~/.config/i3/config'])
	subprocess.run(['startx'])
    