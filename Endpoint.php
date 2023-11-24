<?php
include 'Conexion.php';
header('Access-Control-Allow-Origin:  *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); 

//json_encode(file_get_contents('php://input'));
//if ($_SERVER['REQUEST_METHOD'] == 'POST') {
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
                $fecha = setFecha($input['fechaN']);
                $pass = password_hash($input['pass'], PASSWORD_DEFAULT);
                $d = $conn->newUserBasic($input['nickname'], $pass, $input['nombres'], $input['apellidoP'], $input['apellidoM'], $fecha, $input['correo']);
                //$input['nickname'], $pass, $input['nombres'], $input['apellidoP'], $input['apellidoM'], $fechaN, $input['correo']
                if ($d['estatus'] == 'ok')
                    $data = [
                        'action' => 'singup',
                        'estatus' => 'ok'
                    ];
                 else
                    $data = [
                        'action' => 'singup',
                        'estatus' => 'error'
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
                echo json_encode($d);
                break;
            case 'allPost':
                $d = $conn->allPost($input['id']);
                echo json_encode($d);
                break;
            case 'getUser':
                $data = [
                    action => "getuser",
                    estatus => "ok"
                ];
                echo json_encode($data);
                break;
            case 'prueba':
                $datos = [
                    'fecha' => 'ejemplo',
                    'fecha2' => 'hola'
                ];
            
                echo json_encode($datos);
                /*$promise = function($d) {
                    echo json_encode($d);
                };*/
                //$mensaje = json_encode($datos);
                //promise($mensaje);
                break;
            }
    }

    function setFecha($fechaOriginal){
        $fechaObj = DateTime::createFromFormat('d/m/Y', $fechaOriginal);
        // Reformatear la fecha al formato deseado
        $fechaFormateada = $fechaObj->format('Y-m-d');

        return $fechaFormateada;
    }
//}
?>