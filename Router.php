<?php
include 'funciones.php';
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
                    $existencia = $conn->validate_user($input['nickname']);
                    if($existencia) {
                        $data = [
                            'action' => 'login',
                            'estatus' => 'ok'
                        ];
                        echo json_encode($data);
                    }else{
                        $data = [
                            'action' => 'login',
                            'estatus' => 'error'
                        ];
                        echo json_encode($data);
                    }
                break;
            }
    }
}
?>