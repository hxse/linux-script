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
    subprocess.run(['mkfs.fat','-F32','/dev/sda3'])
    subprocess.run(['mkswap','/dev/sda4'])

text=input('mount /dev/sda... /mnt/...')
if not text:
    subprocess.run(['mkdir','/mnt'])
    subprocess.run(['mount','/dev/sda1','/mnt'])
    subprocess.run(['mkdir','/mnt/home'])
    subprocess.run(['mount','/dev/sda2','/mnt/home'])
    subprocess.run(['mkdir','/mnt/boot'])#vbox default need /mnt/boot
    subprocess.run(['mount','/dev/sda3','/mnt/boot'])
    
text=input('add tuna mirrorlist')
if not text:
    tuna='Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch'
    subprocess.run(['echo',tuna,'>','/etc/pacman.d/mirrorlist'])
    subprocess.run(['pacman', '-Syy'])
    subprocess.run(['reflector ', '--country', 'China','--latest','10','--protocol','https','--sort','rate','--save','/etc/pacman.d/mirrorlist'])
    
text=input('install linux firmware')
if not text:
    subprocess.run(['pacstrap','/mnt','base','base-devel','linux','linux-firmware','nano','dhcpcd'])

text=input('genfstab...')
    subprocess.run(['genfstab', '-U','/mnt','>','/mnt/etc/fstab'])
    subprocess.run(['cat', '/mnt/etc/fstab'])

text =input('run: arch-chroot /mnt')
    subprocess.run(['arch-chroot', '/mnt'])

text=input('vbox uefi')
    subprocess.run(['pacman', '-S','grub','efibootmgr'])
    subprocess.run(['grub-install','--target=x86_64-efi',' --efi-directory=/boot','--bootloader-id=arch_grub'])
    subprocess.run(['grub-mkconfig', '-o','/boot/grub/grub.cfg'])
    
text=input('set password')
    subprocess.run(['passwd'])
    
text=input('add aurcn')
    subprocess.run(['echo','[archlinuxcn]','>>','/etc/pacman.conf'])
    subprocess.run(['echo','Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch','>>','/etc/pacman.conf'])
    subprocess.run(['pacman', '-S','archlinuxcn-keyring'])
    