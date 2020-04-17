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
    .............. HackLabs 0.3 ..............
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
    # -------------------------------------------------------------------------------------- ADD /etc/hosts
    # Opening JSON file
    with open('data.json') as json_file:
        data = json.load(json_file)

        #TODO arrumar loop
        for lfi in data['lfi']:
            add_host(lfi['type'],lfi['address'],lfi['names'])

        for rh in data['rh']:
            add_host(rh['type'],rh['address'],rh['names'])

        for brute_force in data['brute_force']:
            add_host(brute_force['type'],brute_force['address'],brute_force['names'])

        for heartblend in data['heartblend']:
            add_host(heartblend['type'],heartblend['address'],heartblend['names'])

        for juice_shop in data['juice_shop']:
            add_host(juice_shop['type'],juice_shop['address'],juice_shop['names'])

        for dvwa in data['dvwa']:
            add_host(dvwa['type'],dvwa['address'],dvwa['names'])

        for dsvw in data['dsvw']:
            add_host(dsvw['type'],dsvw['address'],dsvw['names'])

        for webgoat in data['webgoat']:
            add_host(webgoat['type'],webgoat['address'],webgoat['names'])
    # -------------------------------------------------------------------------------------- ADD /etc/hosts

    menu_actions['main_menu']()
    sys.exit()

def stopLabs():
    print("Parando Labs")
    subprocess.check_output("docker-compose down".split())
    # -------------------------------------------------------------------------------------- ADD /etc/hosts
    # Opening JSON file
    with open('data.json') as json_file:
        data = json.load(json_file)

        #TODO arrumar loop
        for lfi in data['lfi']:
            del_host(lfi['address'])

        for rh in data['rh']:
            del_host(rh['address'])

        for brute_force in data['brute_force']:
            del_host(brute_force['address'])

        for heartblend in data['heartblend']:
            del_host(heartblend['address'])

        for juice_shop in data['juice_shop']:
            del_host(juice_shop['address'])

        for dvwa in data['dvwa']:
            del_host(dvwa['address'])

        for dsvw in data['dsvw']:
            del_host(dsvw['address'])

        for webgoat in data['webgoat']:
            del_host(webgoat['address'])
    # -------------------------------------------------------------------------------------- ADD /etc/hosts
    menu_actions['main_menu']()
    sys.exit()

# ------------------------------------------------------------------------------------------------------- ADD/REMOVE /etc/hosts
# importing the module
import json
from python_hosts import Hosts, HostsEntry
hosts = Hosts(path='/etc/hosts')

def add_host(type,address,names):
    new_entry = HostsEntry(entry_type=type, address=address, names=[names])
    hosts.add([new_entry])
    hosts.write()

def del_host(address):
    hosts.remove_all_matching(address=address)
    hosts.write()



# ------------------------------------------------------------------------------------------------------- ADD/REMOVE /etc/hosts

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
