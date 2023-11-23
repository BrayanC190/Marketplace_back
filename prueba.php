<?php
require './Conexion.php';
header('Access-Control-Allow-Origin:  *');
header('Access-Control-Allow-Methods: GET');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json');

$prueba = new Conexion();

/*/PRUEBA LOGIN
$estatus = $prueba->validate_user('user1','user1');
    if($estatus){
        $data = [
            'action' => 'login',
            'estatus' => 'ok'
        ];    
    }else {
        $hash = password_hash('user1', PASSWORD_DEFAULT);
        $data = [
            'action' => 'login',
            'estatus' => 'error'
        ];
    }
    echo json_encode($data);*/


/*/PRUEBA CREAR CUENTA
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
        echo json_encode($data);*/
/*/PRUEBA UPDATE CUENTA
    $p = $prueba -> updateUser("user2", "2299102031","5", "1", "2", null, 'boca del rio', 'ver', 'mexico');
    if($p['estatus'] == 'ok')
        $data = [
            'action' => 'update user',
            'estatus' => 'ok'
        ];
        
    else
        $data = [
            'action' => 'update user',
            'estatus' => 'error'
        ];

    echo json_encode($data);
    */

/*/PRUEBA CREAR PUBLICACION
$d = $prueba -> newPost('user2', 'Elote', 2.0, 'pieza','verdura', '2299102030', 'mail.com', null, '1', null, 'venustiano', null, 'boca', 'ver', 'mexico');
echo $d;
*/
/*/PRUEBA SELECT SMALL LOGIN
$d = $prueba->smallPost();
echo json_encode($d);*/

?>