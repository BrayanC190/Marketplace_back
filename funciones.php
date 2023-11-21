<?php
require './Conexion.php';/*
header('Access-Control-Allow-Origin:  *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json');*/

function validate_user($nickname){
    $conexion = new Conexion();
    $existeUsuario = $conexion->validate_user($nickname);
    if ($existeUsuario) {
    echo "El usuario existe.";
    } else {
        echo "El usuario no existe.";
    }
}
?>