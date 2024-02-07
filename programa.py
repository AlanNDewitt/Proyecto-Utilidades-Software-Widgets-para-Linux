#!/usr/bin/env python3.9
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import os


# import time


def portada():
    def destroy_portada():
        text1.destroy()
        text2.destroy()
        text3.destroy()
        text4.destroy()
        boton_siguiente.destroy()

        menu()

    text1 = Label(text="INSTITUTO POLITECNICO NACIONAL", font=("ComicSansMS", 15), bg="#138d75", fg="#212f3c")
    text1.place(x=150, y=20, width=400, height=30)

    text2 = Label(text="ESIME CULHUACAN", font="ComicSansMS", bg="#138d75", fg="#212f3c")
    text2.place(x=270, y=80, width=170, height=25)

    text3 = Label(text="Ing COMPUTACION", font=("ComicSansMS", 13), bg="#138d75", fg="#212f3c")
    text3.place(x=255, y=130, width=210, height=30)

    text4 = Label(text="LINUX FUNDAMENTALS", font=("ComicSansMS", 22), bg="#4a235a", fg="#00e600", )
    text4.place(x=120, y=250, width=450, height=50)

    boton_siguiente = Button(ventana, text="Iniciar", bg="#2c3e50", fg="#76d7c4", font=("Purisa", 15),
                             activebackground="#86f1af", command=destroy_portada)
    boton_siguiente.place(x=250, y=400, width=200, height=30)


def menu():
    # indicador_cargando = Label(text="Cargando ...", font=("Purisa", 15), bg="red", fg="#bc1161")
    # indicador_listo = Label(text="Listo !", font=("Purisa", 15), bg="green", fg="#bc1161")

    def destroy_menu():
        text5.place_forget()
        boton_actuializaOS.place_forget()
        boton_instala_prg.place_forget()
        boton_desinstala_prg.place_forget()
        boton_prg_consola.place_forget()
        boton_salir_prg.place_forget()

    def create_menu():
        text5.place(x=240, y=20, width=200, height=30)
        boton_actuializaOS.place(x=200, y=100, width=270, height=30)
        boton_instala_prg.place(x=200, y=150, width=270, height=30)
        boton_desinstala_prg.place(x=200, y=200, width=270, height=30)
        boton_prg_consola.place(x=200, y=250, width=270, height=30)

        boton_salir_prg.place(x=200, y=400, width=100, height=30)

    def actualizaRyP():
        # sudo -A , para mas info, askpass es una herramienta que permite usar progrma auxiliar para preguntar contra
        os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y update && sudo apt-get -y upgrade")
        os.system("clear")
        print("HECHO !")

    def install_p():
        def inst_libreOffice():
            os.system(
                "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A add-apt-repository ppa:libreoffice && apt -y update && apt -y install libreoffice")
            os.system("clear")
            print("HECHO !")

        def inst_builtessential():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y install build-essential")
            os.system("clear")
            print("HECHO !")

        def inst_diskanalizer():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y install filelight")
            os.system("filelight")
            os.system("clear")
            print("HECHO !")

        def inst_python():
            os.system(
                "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt install software-properties-common && add-apt-repository ppa:deadsnakes/ppa && apt -y install python3.9")
            os.system("clear")
            os.system("python3.9 --version")
            print("HECHO !")

        def inst_shotcut():
            os.system(
                "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A add-apt-repository ppa:haraldhv/shotcut && sudo apt -y update && sudo apt -y install shotcut")
            os.system("clear")
            os.system("shotcut")
            print("HECHO !")

        def inst_chromium():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y install chromium-browser")
            os.system("clear")
            os.system("chromium-browser")
            print("HECHO !")

        def inst_vlc():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y install vlc")
            os.system("clear")
            print("HECHO !")

        def inst_gimp():
            os.system(
                "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A add-apt-repository ppa:ubuntuhandbook1/gimp -y && sudo apt -y update && sudo apt-get -y install gimp")
            os.system("clear")
            print("HECHO !")

        def inst_kazam():
            os.system(
                "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y install python3-cairo python3-xlib && sudo apt -y update && sudo apt -y install kazam")
            os.system("clear")
            print("HECHO !")

        def inst_blender():
            os.system(
                "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A add-apt-repository ppa:thomas-schiex/blender -y && sudo apt-get -y update && sudo apt-get -y install blender")
            os.system("clear")
            print("HECHO !")

        def inst_audacity():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A add-apt-repository ppa:ubuntuhandbook1/audacity -y && sudo apt-get -y update && sudo apt-get -y install audacity")
            print("HECHO !")

        def inst_okular():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A add-apt-repository universe -y && sudo apt-get -y update && sudo apt-get -y install okular")
            print("HECHO !")

        def inst_codeblocks():
            os.system( "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A add-apt-repository universe -y && sudo apt -y update && sudo apt -y install codeblocks")
            print("HECHO !")

        def inst_emacs():
            os.system( "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A add-apt-repository universe -y && sudo apt -y install emacs")
            print("HECHO !")

        def inst_stellarium():
            os.system( "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A add-apt-repository ppa:stellarium/stellarium-releases -y && sudo apt -y update && sudo apt -y install stellarium")
            print("HECHO !")

        def salir_install():
            titulo_install.place_forget()
            radb1.place_forget()
            radb2.place_forget()
            radb3.place_forget()
            radb4.place_forget()
            radb5.place_forget()
            radb6.place_forget()
            radb7.place_forget()
            radb8.place_forget()
            radb9.place_forget()
            radb10.place_forget()
            radb11.place_forget()
            radb12.place_forget()
            radb13.place_forget()
            radb14.place_forget()
            radb15.place_forget()

            salir.place_forget()
            create_menu()

        destroy_menu()

        titulo_install = Label(text="Programas a Instalar", font=("Dyuthi", 20), bg="#2c8ba5", fg="#bc1161")
        titulo_install.place(x=200, y=20, width=330, height=30)

        opcion = IntVar()

        radb1 = Radiobutton(ventana, text="Libre Office", variable=opcion, font=("ArialBlack", 10), bg="#5aab96",
                            value=1, command=inst_libreOffice)
        radb1.place(x=100, y=90, width=200, height=30)
        radb2 = Radiobutton(ventana, text="Built Essentials", variable=opcion, font=("ArialBlack", 10), bg="#5aab96",
                            value=2, command=inst_builtessential)
        radb2.place(x=100, y=120, width=200, height=30)
        radb3 = Radiobutton(ventana, text="Disk Analizer", variable=opcion, font=("ArialBlack", 10), bg="#5aab96",
                            value=3, command=inst_diskanalizer)
        radb3.place(x=100, y=150, width=200, height=30)
        radb4 = Radiobutton(ventana, text="Python 3.9", variable=opcion, font=("ArialBlack", 10), bg="#5aab96",
                            value=4, command=inst_python)
        radb4.place(x=100, y=180, width=200, height=30)
        radb5 = Radiobutton(ventana, text="ShotCut Video Editor ", variable=opcion, font=("ArialBlack", 10),
                            bg="#5aab96",
                            value=5, command=inst_shotcut)
        radb5.place(x=100, y=210, width=200, height=30)
        radb6 = Radiobutton(ventana, text="Chromium Navegador", variable=opcion, font=("ArialBlack", 10),
                            bg="#5aab96", value=6, command=inst_chromium)
        radb6.place(x=100, y=240, width=200, height=30)
        radb7 = Radiobutton(ventana, text="VLC Reproductor ", variable=opcion, font=("ArialBlack", 10),
                            bg="#5aab96", value=7, command=inst_vlc)
        radb7.place(x=100, y=270, width=200, height=30)

        radb8 = Radiobutton(ventana, text="Gimp Editor Image", variable=opcion, font=("ArialBlack", 10),
                            bg="#5aab96",
                            value=8, command=inst_gimp)
        radb8.place(x=100, y=300, width=200, height=30)

        radb9 = Radiobutton(ventana, text="Kzam Graba Desktop", variable=opcion, font=("ArialBlack", 10), bg="#5aab96",
                            value=9, command=inst_kazam)
        radb9.place(x=100, y=330, width=200, height=30)

        radb10 = Radiobutton(ventana, text="Blender 3D creator", variable=opcion, font=("ArialBlack", 10), bg="#5aab96",
                             value=10, command=inst_blender)
        radb10.place(x=100, y=360, width=200, height=30)

        radb11 = Radiobutton(ventana, text="Audacity Audio Editor", variable=opcion, font=("ArialBlack", 10),
                             bg="#5aab96",
                             value=11, command=inst_audacity)
        radb11.place(x=380, y=90, width=210, height=30)

        radb12 = Radiobutton(ventana, text="Okular Document Viewer", variable=opcion, font=("ArialBlack", 10),
                             bg="#5aab96",
                             value=12, command=inst_okular)
        radb12.place(x=380, y=120, width=210, height=30)

        radb13 = Radiobutton(ventana, text="Codeblocks IDE c/c++", variable=opcion, font=("ArialBlack", 10),
                             bg="#5aab96",
                             value=13, command=inst_codeblocks)
        radb13.place(x=380, y=150, width=210, height=30)

        radb14 = Radiobutton(ventana, text="Emacs GNU Text Editor", variable=opcion, font=("ArialBlack", 10),
                             bg="#5aab96",
                             value=14, command=inst_emacs)
        radb14.place(x=380, y=180, width=210, height=30)

        radb15 = Radiobutton(ventana, text="Stellarium Planetario", variable=opcion, font=("ArialBlack", 10),
                             bg="#5aab96",
                             value=15, command=inst_stellarium)
        radb15.place(x=380, y=210, width=210, height=30)

        salir = Button(ventana, text="SALIR", bg="#f5574a", fg="#000000",
                       font=("ArialBlack", 12), activebackground="#e5f54a",
                       command=salir_install)
        salir.place(x=230, y=450, width=210, height=30)



    def desinstall_p():
        print("ola")

        def selec():
            print("comando")

        def desinst_libreOffice():
            os.system(
                "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt purge -y libreoffice*")
            os.system("clear")
            print("HECHO !")

        def desinst_builtessential():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y remove build-essential")
            os.system("clear")
            print("HECHO !")

        def desinst_diskanalizer():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y remove filelight")
            os.system("filelight")
            os.system("clear")
            print("HECHO !")

        def desinst_python():
            os.system(
                "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y remove software-properties-common  && apt -y remove python3.9")
            os.system("clear")
            os.system("python3.9 --version")
            print("HECHO !")

        def desinst_shotcut():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y remove shotcut")
            os.system("clear")
            os.system("shotcut")
            print("HECHO !")

        def desinst_chromium():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y remove chromium-browser")
            os.system("clear")
            os.system("chromium-browser")
            print("HECHO !")

        def desinst_vlc():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y remove vlc")
            os.system("clear")
            print("HECHO !")

        def desinst_gimp():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove gimp")
            os.system("clear")
            print("HECHO !")

        def desinst_kazam():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove kazam")
            os.system("clear")
            print("HECHO !")

        def desinst_blender():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y remove blender")
            os.system("clear")
            print("HECHO !")

        def desinst_audacity():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y remove audacity")
            print("HECHO !")

        def desinst_okular():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt-get -y remove okular")
            print("HECHO !")

        def desinst_codeblocks():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove codeblocks")
            print("HECHO !")

        def desinst_emacs():
            os.system( "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove emacs")
            print("HECHO !")

        def desinst_stellarium():
            os.system( "SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove stellarium")
            print("HECHO !")

        def salir_desinstall():
            titulo_desinstall.place_forget()
            radb1.place_forget()
            radb2.place_forget()
            radb3.place_forget()
            radb4.place_forget()
            radb5.place_forget()
            radb6.place_forget()
            radb7.place_forget()
            radb8.place_forget()
            radb9.place_forget()
            radb10.place_forget()
            radb11.place_forget()
            radb12.place_forget()
            radb13.place_forget()
            radb14.place_forget()
            radb15.place_forget()

            salir.place_forget()
            create_menu()

        destroy_menu()

        titulo_desinstall = Label(text="Programas a Desinstalar", font=("Dyuthi", 20), bg="#27ae60", fg="#bc1161")
        titulo_desinstall.place(x=200, y=20, width=330, height=30)

        opcion = IntVar()

        radb1 = Radiobutton(ventana, text="Libre Office", variable=opcion, font=("ArialBlack", 10), bg="#ec7063",
                            value=1, command=desinst_libreOffice)
        radb1.place(x=100, y=90, width=200, height=30)
        radb2 = Radiobutton(ventana, text="Built Essentials", variable=opcion, font=("ArialBlack", 10), bg="#ec7063",
                            value=2, command=desinst_builtessential)
        radb2.place(x=100, y=120, width=200, height=30)
        radb3 = Radiobutton(ventana, text="Disk Analizer", variable=opcion, font=("ArialBlack", 10), bg="#ec7063",
                            value=3, command=desinst_diskanalizer)
        radb3.place(x=100, y=150, width=200, height=30)
        radb4 = Radiobutton(ventana, text="Python 3.9", variable=opcion, font=("ArialBlack", 10), bg="#ec7063",
                            value=4, command=desinst_python)
        radb4.place(x=100, y=180, width=200, height=30)
        radb5 = Radiobutton(ventana, text="ShotCut Video Editor", variable=opcion, font=("ArialBlack", 10),
                            bg="#ec7063",
                            value=5, command=desinst_shotcut)
        radb5.place(x=100, y=210, width=200, height=30)
        radb6 = Radiobutton(ventana, text="Chromium Navegador", variable=opcion, font=("ArialBlack", 10), bg="#ec7063",
                            value=6, command=desinst_chromium)
        radb6.place(x=100, y=240, width=200, height=30)
        radb7 = Radiobutton(ventana, text="VLC Reproductor", variable=opcion, font=("ArialBlack", 10), bg="#ec7063",
                            value=7, command=desinst_vlc)
        radb7.place(x=100, y=270, width=200, height=30)

        radb8 = Radiobutton(ventana, text="Gimp Editor Image", variable=opcion, font=("ArialBlack", 10), bg="#ec7063",
                            value=8, command=desinst_gimp)
        radb8.place(x=100, y=300, width=200, height=30)

        radb9 = Radiobutton(ventana, text="Kzam Graba Desktop", variable=opcion, font=("ArialBlack", 10), bg="#ec7063",
                            value=9, command=desinst_kazam)
        radb9.place(x=100, y=330, width=200, height=30)

        radb10 = Radiobutton(ventana, text="Blender 3D creator", variable=opcion, font=("ArialBlack", 10), bg="#ec7063",
                             value=10, command=desinst_blender)
        radb10.place(x=100, y=360, width=200, height=30)

        radb11 = Radiobutton(ventana, text="Audacity Audio Editor", variable=opcion, font=("ArialBlack", 10),
                             bg="#ec7063",
                             value=11, command=desinst_audacity)
        radb11.place(x=380, y=90, width=210, height=30)

        radb12 = Radiobutton(ventana, text="Okular Document Viewer", variable=opcion, font=("ArialBlack", 10),
                             bg="#ec7063",
                             value=12, command=desinst_okular)
        radb12.place(x=380, y=120, width=210, height=30)

        radb13 = Radiobutton(ventana, text="Codeblocks IDE c/c++", variable=opcion, font=("ArialBlack", 10),
                             bg="#ec7063",
                             value=13, command=desinst_codeblocks)
        radb13.place(x=380, y=150, width=210, height=30)

        radb14 = Radiobutton(ventana, text="Emacs GNU Text Editor", variable=opcion, font=("ArialBlack", 10),
                             bg="#ec7063",
                             value=14, command=desinst_emacs)
        radb14.place(x=380, y=180, width=210, height=30)

        radb15 = Radiobutton(ventana, text="Stellarium Planetario", variable=opcion, font=("ArialBlack", 10),
                             bg="#ec7063",
                             value=15, command=desinst_stellarium)
        radb15.place(x=380, y=210, width=210, height=30)

        salir = Button(ventana, text="SALIR", bg="#85c1e9", fg="#000000",
                       font=("ArialBlack", 12), activebackground="#e5f54a",
                       command=salir_desinstall)
        salir.place(x=230, y=450, width=210, height=30)

    def salida():
        destroy_menu()
        label_de_fondo.destroy()
        print("adios")

        # ventana.quit()
        label_de_fondoF.place(x=0, y=0, relwidth=1, relheight=1)
        # label_de_fondoF.after(3000,ventana.quit())

    def console_prg():

        def salir_console_prg():

            titulo_console_prg.place_forget()
            neofetch.place_forget()
            neofetch_install.place_forget()
            neofetch_desinstall.place_forget()

            cpufetch.place_forget()
            cpufetch_install.place_forget()
            cpufetch_desinstall.place_forget()

            banner.place_forget()
            banner_install.place_forget()
            banner_desinstall.place_forget()

            bb.place_forget()
            bb_install.place_forget()
            bb_desinstall.place_forget()

            cowsay.place_forget()
            cowsay_install.place_forget()
            cowsay_desinstall.place_forget()

            cmatrix.place_forget()
            cmatrix_install.place_forget()
            cmatrix_desinstall.place_forget()

            Konsole.place_forget()
            Konsole_install.place_forget()
            Konsole_desinstall.place_forget()

            retro_term.place_forget()
            retro_term_install.place_forget()
            retro_term_desinstall.place_forget()

            games.place_forget()
            games_install.place_forget()
            games_desinstall.place_forget()




            salir.place_forget()

            create_menu()
        def neofetch_install():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y update && sudo apt -y install neofetch")
            print("HECHO !")

        def neofetch_desinstall():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove neofetch")
            print("HECHO !")

        def cpufetch_install():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt install git && git clone https://github.com/Dr-Noob/cpufetch && cd cpufetch/ && make && sudo mv cpufetch /usr/local/bin/")
            print("HECHO !")

        def cpufetch_desinstall():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A rm /usr/local/bin/cpufetch | rm -r cpufetch")
            print("HECHO !")

        def banner_install():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y update && sudo apt -y install sysvbanner")
            print("HECHO !")

        def banner_desinstall():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove sysvbanner")
            print("HECHO !")

        def bb_install():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y update && sudo apt -y install bb")
            print("HECHO !")

        def bb_desinstall():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove bb")
            print("HECHO !")

        def cowsay_install():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y update && sudo apt -y install cowsay")
            print("HECHO !")

        def cowsay_desinstall():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove cowsay")
            print("HECHO !")

        def matrix_install():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y update && sudo apt -y install cmatrix")
            print("HECHO !")

        def matrix_desinstall():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove cmatrix")
            print("HECHO !")

        def konsole_install():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y update && sudo apt -y install konsole")
            print("HECHO !")

        def konsole_desinstall():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove konsole")
            print("HECHO !")

        def retro_term_install():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y update && sudo apt -y install cool-retro-term")
            print("HECHO !")

        def retro_term_desinstall():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove cool-retro-term")
            print("HECHO !")

        def console_games_install():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y update && sudo apt -y install games-console")
            print("HECHO !")

        def console_games_desinstall():
            os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y remove games-console")
            print("HECHO !")

        destroy_menu()

        titulo_console_prg = Label(text="Programas de Consola", font=("Consolas", 20), bg="#1e8449", fg="#eaecee")
        titulo_console_prg.place(x=200, y=20, width=330, height=30)

        neofetch = Label(text="Neofetch", font=("ArialBlack", 12), bg="#687059", fg="#4cf1ec")
        neofetch.place(x=80, y=100, width=100, height=30)

        neofetch_install = Button(ventana, text="Instalar", bg="#1fe42e", fg="#000000",font=("ComicSansMS", 10),
                                  activebackground="#7dcea0",command=neofetch_install)
        neofetch_install.place(x=50, y=140, width=80, height=30)

        neofetch_desinstall = Button(ventana, text="Desinstalar", bg="#f1948a", fg="#000000", font=("ComicSansMS", 10),
                                  activebackground="#7dcea0", command=neofetch_desinstall)
        neofetch_desinstall.place(x=130, y=140, width=80, height=30)



        cpufetch = Label(text="CPUfetch", font=("ArialBlack", 12), bg="#687059", fg="#4cf1ec")
        cpufetch.place(x=80, y=200, width=100, height=30)

        cpufetch_install = Button(ventana, text="Instalar", bg="#1fe42e", fg="#000000", font=("ComicSansMS", 10),
                                  activebackground="#7dcea0", command=cpufetch_install)
        cpufetch_install.place(x=50, y=240, width=80, height=30)

        cpufetch_desinstall = Button(ventana, text="Desinstalar", bg="#f1948a", fg="#000000", font=("ComicSansMS", 10),
                                     activebackground="#7dcea0", command=cpufetch_desinstall)
        cpufetch_desinstall.place(x=130, y=240, width=80, height=30)


        banner = Label(text="Banner", font=("ArialBlack", 12), bg="#687059", fg="#4cf1ec")
        banner.place(x=80, y=300, width=100, height=30)

        banner_install = Button(ventana, text="Instalar", bg="#1fe42e", fg="#000000", font=("ComicSansMS", 10),
                                  activebackground="#7dcea0", command=banner_install)
        banner_install.place(x=50, y=340, width=80, height=30)

        banner_desinstall = Button(ventana, text="Desinstalar", bg="#f1948a", fg="#000000", font=("ComicSansMS", 10),
                                     activebackground="#7dcea0", command=banner_desinstall)
        banner_desinstall.place(x=130, y=340, width=80, height=30)



        bb = Label(text="BB art ASCII", font=("ArialBlack", 12), bg="#687059", fg="#4cf1ec")
        bb.place(x=280, y=100, width=120, height=30)

        bb_install = Button(ventana, text="Instalar", bg="#1fe42e", fg="#000000", font=("ComicSansMS", 10),
                                  activebackground="#7dcea0", command=bb_install)
        bb_install.place(x=250, y=140, width=80, height=30)

        bb_desinstall = Button(ventana, text="Desinstalar", bg="#f1948a", fg="#000000", font=("ComicSansMS", 10),
                                     activebackground="#7dcea0", command=bb_desinstall)
        bb_desinstall.place(x=330, y=140, width=80, height=30)


        cowsay = Label(text="Cowsay", font=("ArialBlack", 12), bg="#687059", fg="#4cf1ec")
        cowsay.place(x=280, y=200, width=120, height=30)

        cowsay_install = Button(ventana, text="Instalar", bg="#1fe42e", fg="#000000", font=("ComicSansMS", 10),
                            activebackground="#7dcea0", command=cowsay_install)
        cowsay_install.place(x=250, y=240, width=80, height=30)

        cowsay_desinstall = Button(ventana, text="Desinstalar", bg="#f1948a", fg="#000000", font=("ComicSansMS", 10),
                               activebackground="#7dcea0", command=cowsay_desinstall)
        cowsay_desinstall.place(x=330, y=240, width=80, height=30)



        cmatrix = Label(text="Matrix", font=("ArialBlack", 12), bg="#687059", fg="#4cf1ec")
        cmatrix.place(x=280, y=300, width=120, height=30)

        cmatrix_install = Button(ventana, text="Instalar", bg="#1fe42e", fg="#000000", font=("ComicSansMS", 10),
                                activebackground="#7dcea0", command=matrix_install)
        cmatrix_install.place(x=250, y=340, width=80, height=30)

        cmatrix_desinstall = Button(ventana, text="Desinstalar", bg="#f1948a", fg="#000000", font=("ComicSansMS", 10),
                                   activebackground="#7dcea0", command=matrix_desinstall)
        cmatrix_desinstall.place(x=330, y=340, width=80, height=30)


        Konsole = Label(text="Konsole Terminal", font=("ArialBlack", 12), bg="#687059", fg="#4cf1ec")
        Konsole.place(x=450, y=100, width=160, height=30)

        Konsole_install = Button(ventana, text="Instalar", bg="#1fe42e", fg="#000000", font=("ComicSansMS", 10),
                                  activebackground="#7dcea0", command=konsole_install)
        Konsole_install.place(x=450, y=140, width=80, height=30)

        Konsole_desinstall = Button(ventana, text="Desinstalar", bg="#f1948a", fg="#000000", font=("ComicSansMS", 10),
                                     activebackground="#7dcea0", command=konsole_desinstall)
        Konsole_desinstall.place(x=530, y=140, width=80, height=30)


        retro_term = Label(text="Retro Terminal", font=("ArialBlack", 12), bg="#687059", fg="#4cf1ec")
        retro_term.place(x=460, y=200, width=140, height=30)

        retro_term_install = Button(ventana, text="Instalar", bg="#1fe42e", fg="#000000", font=("ComicSansMS", 10),
                                activebackground="#7dcea0", command=retro_term_install)
        retro_term_install.place(x=450, y=240, width=80, height=30)

        retro_term_desinstall = Button(ventana, text="Desinstalar", bg="#f1948a", fg="#000000", font=("ComicSansMS", 10),
                                   activebackground="#7dcea0", command=retro_term_desinstall)
        retro_term_desinstall.place(x=530, y=240, width=80, height=30)


        games = Label(text="Console Games", font=("ArialBlack", 12), bg="#687059", fg="#4cf1ec")
        games.place(x=460, y=300, width=150, height=30)

        games_install = Button(ventana, text="Instalar", bg="#1fe42e", fg="#000000", font=("ComicSansMS", 10),
                                 activebackground="#7dcea0", command=console_games_install)
        games_install.place(x=450, y=340, width=80, height=30)

        games_desinstall = Button(ventana, text="Desinstalar", bg="#f1948a", fg="#000000", font=("ComicSansMS", 10),
                                    activebackground="#7dcea0", command=console_games_desinstall)
        games_desinstall.place(x=530, y=340, width=80, height=30)




        salir = Button(ventana, text="SALIR", bg="#bb8fce", fg="#000000",font=("ArialBlack", 12),
                       activebackground="#f7dc6f",command=salir_console_prg)
        salir.place(x=530, y=450, width=150, height=30)






    # ---------------------------Secuencia Principal Menu----------------------------------------------------
    print("hola")
    text5 = Label(text="MENU", font=("ComicSansMS", 20), bg="#bb8fce", fg="#212f3c")
    text5.place(x=240, y=20, width=200, height=30)

    boton_actuializaOS = Button(ventana, text="Actualiza Repos y Programas", bg="#7f32f6", fg="#2ef72b",
                                font=("ArialBlack", 12),
                                command=actualizaRyP)
    boton_actuializaOS.place(x=200, y=100, width=270, height=30)

    boton_instala_prg = Button(ventana, text="Instalar Programas", bg="#7f32f6", fg="#2ef72b",
                               font=("ArialBlack", 12),
                               command=install_p)
    boton_instala_prg.place(x=200, y=150, width=270, height=30)

    boton_desinstala_prg = Button(ventana, text="Desinstalar Programas", bg="#7f32f6", fg="#2ef72b",
                                  font=("ArialBlack", 12),
                                  command=desinstall_p)
    boton_desinstala_prg.place(x=200, y=200, width=270, height=30)

    boton_prg_consola = Button(ventana, text="Programas Consola", bg="#7f32f6", fg="#2ef72b",
                               font=("ArialBlack", 12),
                               command=console_prg)
    boton_prg_consola.place(x=200, y=250, width=270, height=30)

    boton_salir_prg = Button(ventana, text="Salir", bg="red", fg="#2ef72b",
                             font=("ArialBlack", 12),
                             command=salida)
    boton_salir_prg.place(x=200, y=400, width=100, height=30)


# ----------------------------------------SECUENCIA PRINCIPAL

os.system("SUDO_ASKPASS=/usr/bin/ssh-askpass sudo -A apt -y install espeak && sudo apt -y install xcowsay")
os.system("espeak Hola")
os.system("xcowsay --image=tux.jpg --time 1 hola")


ventana = tk.Tk()
# ventana.config(bg = "purple")
ventana.title("Linux Fundamentals")
ventana.geometry("700x500")
ventana.config(cursor="pirate")

fuente_titulos = tkFont.Font(family="Comic Sans MS", size=25, weight="bold", slant="italic")

background = PhotoImage(file="fondo.png")
label_de_fondo = Label(ventana, image=background)
label_de_fondo.place(x=0, y=0, relwidth=1, relheight=1)

backgroundF = PhotoImage(file="Fondo2.png")
label_de_fondoF = Label(ventana, image=backgroundF)

portada()

ventana.mainloop()

# -------------------------------------------SECUENCIA PRINCIPAL
