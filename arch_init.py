import subprocess

text=input('print fdisk -l')
if not text:
    subprocess.run(['fdisk', '-l'])
    
text=input('*input: cfdisk /dev/sda{x} \n please fllow: sda1->/mnt sda2->/mnt/home sda3->efi')
if not text:
    subprocess.run(['cfdisk',text])
    
text=input('mkfs disk')
    subprocess.run(['mkfs.ext4','/dev/sda1'])
    subprocess.run(['mkfs.ext4','/dev/sda2'])
    subprocess.run(['mkfs.ext4','/dev/sda3'])
    subprocess.run(['mkswap','/dev/sda4'])

text=input('mount /dev/sda... /mnt/...')
if not text:
    subprocess.run(['mkdir','/mnt'])
    subprocess.run(['mount','/dev/sda1','/mnt'])
    subprocess.run(['mkdir','/mnt/home'])
    subprocess.run(['mount','/dev/sda2','/mnt/home'])
    subprocess.run(['mkdir','/mnt/efi'])
    subprocess.run(['mount','/dev/sda2','/mnt/efi'])
    
text=input('add tuna mirrorlist')
if not text:
    tuna='Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch'
    subprocess.run(['echo',tuna,'>','/etc/pacman.d/mirrorlist'])
    subprocess.run(['pacman', '-Syy'])

text=input('install linux firmware')
if not text:
    subprocess.run(['pacstrap','/mnt','base','linux','linux-firmware','nano','base-devel'])

text=input('genfstab...')
    subprocess.run(['genfstab', '-U','/mnt','>','/mnt/etc/fstab'])
    subprocess.run(['cat', '/mnt/etc/fstab'])

text=input('arch-chroot /mnt')
    subprocess.run(['arch-chroot', '/mnt'])
    
