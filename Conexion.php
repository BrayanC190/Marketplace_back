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

    public function validate_user($nickname) {
        try {
            $stmt = $this->conn->prepare("SELECT COUNT(*) FROM usuarios WHERE nickname = :nickname");
            $stmt->bindParam(':nickname', $nickname, PDO::PARAM_STR);
            $stmt->execute();

            $result = $stmt->fetchColumn();
            return $result > 0;
        } catch(PDOException $e) {
            die("Error en la consulta: " . $e->getMessage());
        }
    }
}
?>