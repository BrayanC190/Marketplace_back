<?php
class Conexion {
    private const SERVERNAME = "tecnm.c1etdihcwq78.us-east-2.rds.amazonaws.com";
    private const DBNAME = "marketplace";
    private const USERNAME = "admin";
    private const PASSWORD = "TECNM123";
    private $conn; 

    public function __construct() {
        try {
            $this->conn = new PDO("mysql:host=" . self::SERVERNAME . ";dbname=" . self::DBNAME, self::USERNAME, self::PASSWORD);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $e) {
            die("Connection failed: " . $e->getMessage());
        }
    }

    function __destruct() {       
        $this->conn = null;
    }

    public function validate_user($nickname, $pass) {
        try {
            $stmt = $this->conn->prepare("SELECT pass FROM usuarios WHERE nickname = :nickname");
            $stmt->bindParam(':nickname', $nickname, PDO::PARAM_STR);
            $stmt->execute();
    
            if ($stmt->rowCount() > 0) {
                $hashedPassword = $stmt->fetch(PDO::FETCH_ASSOC)['pass'];
    
                // Utiliza password_verify para comparar el hash de la contraseña con la contraseña proporcionada
                return password_verify($pass, $hashedPassword);
            } else {
                // El usuario no existe
                return false;
            }
        } catch(PDOException $e) {
            die("Error en la consulta: " . $e->getMessage());
        }
    }

    public function newUserBasic($nickname, $hashedPassword, $nombres, $apellidoP, $apellidoM, $fechaN, $correo){
        try{
        $stmt = $this->conn->prepare("CALL newUserBasic(:nickname, :pass, :Nombres, :ApellidoP, :ApellidoM, :FechaN, :Correo)");

        $stmt->bindParam(':nickname', $nickname);
        $stmt->bindParam(':pass', $hashedPassword); 
        $stmt->bindParam(':Nombres', $nombres);
        $stmt->bindParam(':ApellidoP', $apellidoP);
        $stmt->bindParam(':ApellidoM', $apellidoM);
        $stmt->bindParam(':FechaN', $fechaN);
        $stmt->bindParam(':Correo', $correo);

        $stmt->execute();
        $data = ['estatus' => 'ok'];
        return $data;
        }catch(PDOException $e) {
            $data = [
                'estatus' => 'error',
                'getMessage' => $e->getMessage()
            ];
            //die();
            return $data;
        }
    }
    
}
?>