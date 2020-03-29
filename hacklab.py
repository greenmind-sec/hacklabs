#!/usr/bin/python3
# Load
from sys import stdout, exit
from time import sleep


import sys, os ,time , subprocess, argparse
# -*- coding: utf-8 -*-
#title           :hacklabs.py
#description     :Labs para estudos.
#author          :GreenMind
#date            :28 Março 2020
#version         :0.1
#usage           :sudo python3 hacklabs.py
#python version  :3.4.2
#
#=======================================================================
#
#
#=======================================================================
#--
# Mensagens
#--
#Mensagem "LOGO"
#--
msg_thc='''
                         .
                         C
                        GC;
       :               .CCC
        G              fCLC1
        ;CC           1CCLCC              1
        ,CLCG         LCCCCL           fC:
         LCCCCt       GCCCCC        :CLCi
          CCCCCC.     CCCCCC,     fCCCCL
           CCCCCC;    CCCCCC    GCCLCC;
           .CCCCCCf   iCCCCC  CCCCCCC
 .,          tCCCCCG  iCCCCG CCCCCCC
   ,CCCGC;    tCCLCCC .CCCCCtCCCCCf
     ,CLLCCCC1  LCCCC1 GCCC.CLCCL
       ,fCCCCCCCf;LCLC.CCC;CLCG    ,GCCCCCCLCCG.
          .GCCCCCCCC1GC CG1LG :GCCCCCGCCCCt,
    .............. HackLabs 0.2 ..............
'''
#--
#MSG Menu Principal
#--
msg_main_menu='''
%s
    1) Labs Check
    2) Labs Start
    3) Labs Stop
  sair) Sair
'''%(msg_thc)
#
#=======================================================================
# definição Main - constantes
menu_actions  = {}
# =======================
# FUNÇÕES MENUS
# =======================

def check_docker():
    if 256 != os.system('which docker'):
    	print("OK.")
    else:
    	print("FAIL")
    	sys.exit()

def check_root():
    # Check root
    if os.geteuid() != 0:
        print("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
        sys.exit()
    else:
        parser = argparse.ArgumentParser(description = 'HackLab')

def check_load():
    RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
    for i in range(101):
    	sleep(0.01)
    	stdout.write("\r{0}[{1}*{0}]{1} Preparing environment... %d%%".format(CYAN, END) % i)
    	stdout.flush()

# Check Docker and ROOT
check_docker()
check_root()
check_load()


#--
# Função Menu principal
#--
def main_menu():
    os.system('clear')
    print(msg_main_menu)
    choice = input(" >>  ")
    exec_menu(choice)
    return
#--
# Função executa menu
#--
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return
#
#--
# Função Voltar ao menu principal
#--
def back():
    menu_actions['main_menu']()
#--
# Função Sair programa
#--
def exit():
    os.system("clear")
    print("O hacklab foi finalizado com segurança!")
    sys.exit()

def menu1():
    print("Menu 1")
    check_load()
    sys.exit()

def startLabs():
    print("Iniciando Labs")
    subprocess.check_output("docker-compose up -d".split())
    menu_actions['main_menu']()
    sys.exit()

def stopLabs():
    print("Parando Labs")
    subprocess.check_output("docker-compose down".split())
    menu_actions['main_menu']()
    sys.exit()

# =======================
# DEFINIÇÃO DE MENUS
# =======================
menu_actions = {
    #--
    # Menu principal
    #--
    'main_menu': main_menu,
    '1': menu1,
    '2': startLabs,
    '3': stopLabs,
    #--
    # Voltar e Sair
    #--
    'voltar': back,
    'sair': exit,
}
# =======================
# MENU PRINCIPAL
# =======================
if __name__ == "__main__":
    main_menu()
