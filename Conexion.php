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

    public function updateUser($nickname, $telefono, $Calle1, $Calle2, $Colonia, $Lote, $Municipio, $Estado, $Pais){
        try{
            $stmt = $this->conn->prepare("CALL updateUser(nickname, telefono, Calle1, Calle2, Colonia, Lote, Municipio, Estado, Pais)");
            
            $stmt->bindParam(':nickname', $nickname);
            $stmt->bindParam(':telefono', $telefono);
            $stmt->bindParam(':Calle1', $Calle1);
            $stmt->bindParam(':Calle2', $Calle2);
            $stmt->bindParam(':Colonia', $Colonia);
            $stmt->bindParam(':Lote', $Lote);
            $stmt->bindParam(':Municipia', $Municipi);
            $stmt->bindParam(':Estado', $Estado);            
            $stmt->bindParam(':Pais', $Pais);   
            $stmt->execute();         
            $data = ['estatus' => 'ok'];
            return $data;
        }catch(PDOException $e){
            $data = [
                'estatus' => 'error',
                'getMessage' => $e->getMessage()
            ];
            return $data;
        }
    }

    public function newPost($nickname, $Nombre, $Precio, $Unidad, $Descripcion, $Telefono,
    $Correo, $Web, $Calle1, $Calle2, $Colonia, $Lote, $Municipio, $Estado, $Pais){
        try{
            //$stmt = $this->conn->prepare("call newPublicacion('user2', 'Elote', 2.2, 'pieza','verdura', '2299102030', 'mail.com', null, '1', null, 'venustiano', null, 'boca', 'ver', 'mexico',@p_referenciaOut);");
            
            $stmt = $this->conn->prepare("call newPublicacion(
                :nickname, :Nombre, :Precio, :Unidad, :Descripcion, :Telefono, :Correo,
                :Web, :Calle1, :Calle2, :Colonia, :Lote, :Municipio,
                :Estado, :Pais, @p_referenciaOut);");
                
            $stmt->bindValue(':nickname', $nickname);
            $stmt->bindValue(':Nombre', $Nombre);
            $stmt->bindValue(':Precio', $Precio);            
            $stmt->bindValue(':Unidad', $Unidad);
            $stmt->bindValue(':Descripcion', $Descripcion);
            $stmt->bindValue(':Telefono', $Telefono);
            $stmt->bindValue(':Correo', $Correo);
            $stmt->bindValue(':Web', $Web);
            $stmt->bindValue(':Calle1', $Calle1);
            $stmt->bindValue(':Calle2', $Calle2);
            $stmt->bindValue(':Colonia', $Colonia);
            $stmt->bindValue(':Lote', $Lote, PDO::PARAM_INT);
            $stmt->bindValue(':Municipio', $Municipio);
            $stmt->bindValue(':Estado', $Estado);
            $stmt->bindValue(':Pais', $Pais);         
            $stmt->execute();

            $stmt = $this->conn->prepare("SELECT @p_referenciaOut;");
            $stmt->execute();

            $select = $stmt->fetchAll(PDO::FETCH_ASSOC);        
                return json_encode($select);
        }catch(PDOException $e){
            $data = [
                'estatus' => 'error',
                'getMessage' => $e->getMessage()
            ];
            return json_encode($data);
        }
    }

    public function smallPost(){
        $stmt = $this->conn->prepare("CALL smallPublicacion()");
        $stmt->execute();
        $data = $stmt->fetchAll(PDO::FETCH_ASSOC);
        $response = json_encode($data);
        return $response;
    }

    public function grandPost(){
        
    }
}
?>