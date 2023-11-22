<?php
require './Conexion.php';
header('Access-Control-Allow-Origin:  *');
header('Access-Control-Allow-Methods: GET');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json');

$prueba = new Conexion();

/*//prueba login
$estatus = $prueba->validate_user('user1','user1');
if($estatus){
    $data = [
        'action' => 'login',
        'estatus' => 'ok'
    ];
    
    echo json_encode($data);
}else {
    $hash = password_hash('user1', PASSWORD_DEFAULT);
    echo $hash;
    echo "error";
}*/

//pureba crear cuenta
    $d = $prueba->newUserBasic('user2', password_hash('user2', PASSWORD_DEFAULT), 'user2','user2', 'user2', '2000-01-01', 'user2@mail.com');
        if ($d['estatus'] == 'ok'){
            $data = [
                'action' => 'singup',
                'estatus' => 'ok'
            ];
        } else {
            $data = [
                'action' => 'singup',
                'estatus' => 'error',
                'message' => $d['getMessage']
            ];
        }                
        echo json_encode($data);


?>