#!/bin/bash

echo "Entre com payload: ";read payload
echo "Entre Com a foto ex(teste.png,teste,jpeg): ";read ex
echo""
echo -e "\e[31m 1- Coloque no comment\e[0m"
echo -e "\e[31m 2- Coloque no Artist\e[0m"
echo -e "\e[31m 3- Coloque no Filter\e[0m"
echo -e "\e[31m 4- Coloque no Interlace\e[0m"
echo -e "\e[31m 5- Coloque no Software\e[0m"
echo -e "\e[31m 6- Coloque no Megapixels\e[0m"
echo ""

read -n2 -p 'Opção: ' OPCAO

case $OPCAO  in 

  1)
    exiftool -Comment="$payload" $ex
    a=$(exiftool $ex)
    echo "Payload inserido --> $a"
    echo ""
    ;;
  2)
    exiftool -Artist="$payload" $ex
    a=$(exiftool $ex)
    echo "Payload inserido --> $a"
    echo ""
    ;;

  3)
    exiftool -Filter="$payload" $ex
    a=$(exiftool $ex)
    echo "Payload inserido --> $a"
    echo ""
    ;;
  4)
    exiftool -Interlace="$payload" $ex
    a=$(exiftool $ex)
    echo "Payload inserido --> $a"
    echo ""
    ;;
  5)
    exiftool -Software="$payload" $ex
    a=$(exiftool $ex)
    echo "Payload inserido --> $a"
    echo ""
    ;;
  6)
    exiftool -Megapixels="$payload" $ex
    a=$(exiftool $ex)
    echo "Payload inserido --> $a"
    echo ""
    ;;
  
esac

