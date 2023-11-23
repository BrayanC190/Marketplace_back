<?php
include 'Conexion.php';
header('Access-Control-Allow-Origin:  *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); 


if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $input = json_decode(file_get_contents('php://input'), true);
    if (isset($input['action'])) {        
        $conn = new Conexion();

        switch ($input['action']) {
            case 'login':
                    //$existencia = $conn->validate_user($input['nickname']);}
                    $existencia = $conn->validate_user($input['nickname'], $input['pass']);
                    if($existencia)
                        $data = [
                            'action' => 'login',
                            'estatus' => 'ok'
                        ];
                    else
                        $data = [
                            'action' => 'login',
                            'estatus' => 'error'
                        ];                                  
                    echo json_encode($data);
                break;
            case 'signup':
                $d = $conn->newUserBasic($input['nickname'], $input['hashedPassword'], $input['nombres'], $input['apellidoP'], $input['apellidoM'], $input['fechaN'], $input['correo']);
                if ($d['estatus'] == 'ok')
                    $data = [
                        'action' => 'singup',
                        'estatus' => 'ok'
                    ];
                 else 
                    $data = [
                        'action' => 'singup',
                        'estatus' => 'error',
                        'message' => $d['getMessage']
                    ];                               
                echo json_encode($data);
                break;
            case 'update':
                $d = $conn -> updateUser($input['nickname'], $input['telefono'], $input['Calle1'], $input['Calle2'],
                $input['Colonia'], $input['Lote'], $input['Municipio'], $input['Estado'], $input['Pais']);
                if($d['estatus'] == 'ok')
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
                break;
            case 'smallPost':
                $d = $conn->smallPost();
                if($d['estatus'] == 'ok')
                    $data = [
                        'action' => 'smallPost',
                        'estatus' => 'ok'
                    ];                    
                else
                    $data = [
                        'action' => 'smallPost',
                        'estatus' => 'error'
                    ];
                echo json_encode($d);
                break;
            }
    }
}
?>