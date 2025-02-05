import os

def reiniciar():
    print("Reiniciando o dispositivo...")
    os.system("reboot")

def configurar_fabrica():
    print("Abrindo configurações de fábrica...")
    os.system("am start -a android.settings.MASTER_CLEAR")

def ativar_oem():
    print("Ativando OEM Unlocking...")
    os.system("settings put global oem_unlock_allowed 1")

def ativar_desenv():
    print("Ativando Modo Desenvolvedor...")
    os.system("am start -a android.settings.APPLICATION_DEVELOPMENT_SETTINGS")

def ativar_debug_usb():
    print("Ativando Depuração USB...")
    os.system("settings put global development_settings_enabled 1")

def abrir_wifi():
    print("Abrindo configurações de Wi-Fi...")
    os.system("am start -a android.settings.WIFI_SETTINGS")

def abrir_bluetooth():
    print("Abrindo configurações de Bluetooth...")
    os.system("am start -a android.settings.BLUETOOTH_SETTINGS")

def abrir_bateria():
    print("Abrindo configurações de Bateria...")
    os.system("am start -a android.settings.BATTERY_SAVER_SETTINGS")

def abrir_localizacao():
    print("Abrindo configurações de Localização...")
    os.system("am start -a android.settings.LOCATION_SOURCE_SETTINGS")

def abrir_entradas():
    print("Abrindo configurações de Entradas (teclado, idioma)...")
    os.system("am start -a android.settings.INPUT_METHOD_SETTINGS")

def abrir_armazenamento():
    print("Abrindo configurações de Armazenamento...")
    os.system("am start -a android.settings.INTERNAL_STORAGE_SETTINGS")

def abrir_aplicativos():
    print("Abrindo configurações de Aplicativos...")
    os.system("am start -a android.settings.APPLICATION_SETTINGS")

def ativar_nfc():
    print("Ativando NFC...")
    os.system("am start -a android.settings.NFC_SETTINGS")

def ativar_bloqueio_tela():
    print("Ativando Bloqueio de Tela...")
    os.system("am start -a android.settings.SECURITY_SETTINGS")

def abrir_sons():
    print("Abrindo configurações de Sons...")
    os.system("am start -a android.settings.SOUND_SETTINGS")

def ativar_autosave():
    print("Ativando Auto Save...")
    os.system("settings put global auto_save 1")

def desativar_autosave():
    print("Desativando Auto Save...")
    os.system("settings put global auto_save 0")

def limpar_cache():
    print("Limpando cache...")
    os.system("pm clear com.android.browser")

def ativar_rota_aplicacao():
    print("Ativando rota de aplicação...")
    os.system("settings put global development_settings_enabled 1")

def ativar_modo_aviao():
    print("Ativando Modo Avião...")
    os.system("svc wifi disable; svc data disable; svc bluetooth disable")

def menu_pt():
    while True:
        print("\nMenu Android (Português)")
        print("1. Reiniciar o celular")
        print("2. Abrir configurações de fábrica")
        print("3. Ativar OEM Unlocking")
        print("4. Ativar Modo Desenvolvedor")
        print("5. Ativar Depuração USB")
        print("6. Abrir configurações de Wi-Fi")
        print("7. Abrir configurações de Bluetooth")
        print("8. Abrir configurações de Bateria")
        print("9. Abrir configurações de Localização")
        print("10. Abrir configurações de Entradas (teclado, idioma)")
        print("11. Abrir configurações de Armazenamento")
        print("12. Abrir configurações de Aplicativos")
        print("13. Ativar NFC")
        print("14. Ativar Bloqueio de Tela")
        print("15. Abrir configurações de Sons")
        print("16. Ativar Auto Save")
        print("17. Desativar Auto Save")
        print("18. Limpar Cache do Navegador")
        print("19. Ativar Rota de Aplicação")
        print("20. Ativar Modo Avião")
        print("21. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            reiniciar()
        elif escolha == '2':
            configurar_fabrica()
        elif escolha == '3':
            ativar_oem()
        elif escolha == '4':
            ativar_desenv()
        elif escolha == '5':
            ativar_debug_usb()
        elif escolha == '6':
            abrir_wifi()
        elif escolha == '7':
            abrir_bluetooth()
        elif escolha == '8':
            abrir_bateria()
        elif escolha == '9':
            abrir_localizacao()
        elif escolha == '10':
            abrir_entradas()
        elif escolha == '11':
            abrir_armazenamento()
        elif escolha == '12':
            abrir_aplicativos()
        elif escolha == '13':
            ativar_nfc()
        elif escolha == '14':
            ativar_bloqueio_tela()
        elif escolha == '15':
            abrir_sons()
        elif escolha == '16':
            ativar_autosave()
        elif escolha == '17':
            desativar_autosave()
        elif escolha == '18':
            limpar_cache()
        elif escolha == '19':
            ativar_rota_aplicacao()
        elif escolha == '20':
            ativar_modo_aviao()
        elif escolha == '21':
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_en():
    while True:
        print("\nAndroid Menu (English)")
        print("1. Restart the phone")
        print("2. Open factory settings")
        print("3. Enable OEM Unlocking")
        print("4. Enable Developer Mode")
        print("5. Enable USB Debugging")
        print("6. Open Wi-Fi settings")
        print("7. Open Bluetooth settings")
        print("8. Open Battery settings")
        print("9. Open Location settings")
        print("10. Open Input settings")
        print("11. Open Storage settings")
        print("12. Open Apps settings")
        print("13. Enable NFC")
        print("14. Enable Screen Lock")
        print("15. Open Sound settings")
        print("16. Enable Auto Save")
        print("17. Disable Auto Save")
        print("18. Clear Browser Cache")
        print("19. Enable App Routing")
        print("20. Enable Airplane Mode")
        print("21. Exit")
        
        escolha = input("Choose an option: ")

        if escolha == '1':
            reiniciar()
        elif escolha == '2':
            configurar_fabrica()
        elif escolha == '3':
            ativar_oem()
        elif escolha == '4':
            ativar_desenv()
        elif escolha == '5':
            ativar_debug_usb()
        elif escolha == '6':
            abrir_wifi()
        elif escolha == '7':
            abrir_bluetooth()
        elif escolha == '8':
            abrir_bateria()
        elif escolha == '9':
            abrir_localizacao()
        elif escolha == '10':
            abrir_entradas()
        elif escolha == '11':
            abrir_armazenamento()
        elif escolha == '12':
            abrir_aplicativos()
        elif escolha == '13':
            ativar_nfc()
        elif escolha == '14':
            ativar_bloqueio_tela()
        elif escolha == '15':
            abrir_sons()
        elif escolha == '16':
            ativar_autosave()
        elif escolha == '17':
            desativar_autosave()
        elif escolha == '18':
            limpar_cache()
        elif escolha == '19':
            ativar_rota_aplicacao()
        elif escolha == '20':
            ativar_modo_aviao()
        elif escolha == '21':
            print("Exiting the menu...")
            break
        else:
            print("Invalid option, try again.")

def escolha_idioma():
    print("Escolha seu idioma / Choose your language")
    print("1. Português")
    print("2. English")
    
    idioma = input("Digite sua escolha: ")
    
    if idioma == '1':
        menu_pt()
    elif idioma == '2':
        menu_en()
    else:
        print("Opção inválida. Saindo...")
        exit()

if __name__ == "__main__":
    escolha_idioma()
