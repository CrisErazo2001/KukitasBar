import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Input, FormGroup, Label } from 'reactstrap';
import s from "../ingredientes/Ingredientes.module.scss";
// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";


const NuevoUsuario = ({ onClose, setUsuarios, usuarios, usuario, modoEditar }) => {
  //Config de Notificaciones
  const options = {
    autoClose: 3000,
    closeButton: false,
    hideProgressBar: true,
    position: toast.POSITION.TOP_CENTER,
  };
  
  const [modifyUserStatus, setModifyUserStatus] = useState({});
  const [nuevoUser, setNuevoUser] = useState({
    id_usuario: 0,
    tipo: '',
    user: '',
    password: '',
    created_at: ''
  });

  useEffect(() => {
    if (modoEditar && usuario) {
      setNuevoUser(usuario);
    } else {
      setNuevoUser({
        id_usuario: 0,
        tipo: '',
        user: '',
        password: '',
        created_at: ''
      });
    }
  }, [usuario, modoEditar]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNuevoUser({ ...nuevoUser, [name]: value });
  };

  

  const handleSubmit = () => {
    if (modoEditar) {
      fetch('/usuario/modificar', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(nuevoUser)
      })
      .then(response => {
          console.log('Respuesta del servidor:', response); // Log de la respuesta
          return response.json();
      })
      .then(data => {
          console.log('Datos recibidos:', data); // Log de los datos recibidos
          setModifyUserStatus(data); // Guarda la respuesta en createIngStatus
          // setIngredientes((prevIngredientes) => [...prevIngredientes, nuevoUser]);
          onClose(); // Llamar a onClose() solo después de recibir la respuesta del servidor
      })
      .catch(error => console.error('Error:', error));
      
    } 
  };

  useEffect(() => {
      console.log('Estado de modifyUserStatus:', modifyUserStatus);
      
      if (modifyUserStatus.code == 200){
        
        toast(
          
          <Notification 
              type={'success'} 
              errorMessage={modifyUserStatus.message} 
              withIcon 
          />, 
          options
        );
        
      }else if (modifyUserStatus.code == 400){
        toast(
          
          <Notification 
              type={'error'} 
              errorMessage={modifyUserStatus.message} 
              withIcon 
          />, 
          options
        );
      } 
  }, [modifyUserStatus]);
;

  return (
    <div>
      <Row>
        <Col>
          <h3>{modoEditar ? 'Editar Usuario' : 'Agregar Nuevo Usuario'}</h3>
          <Row>
            <Col md={6}>
              {modoEditar && (
                <>
                  <Label for="id_usuario">ID del usuario</Label>
                  <Input
                    type="text"
                    id="id_usuario"
                    value={nuevoUser.id_usuario}
                    disabled={modoEditar}
                  />
                </>
              )}
              <FormGroup>
                <Label for="user">Nombre del Usuario</Label>
                <Input type="text" name="user" value={nuevoUser.user} onChange={handleInputChange} />
              </FormGroup>
              
              
            </Col>
            <Col md={6}>
            <FormGroup>
                <Label for="tipo">Categoría</Label>
                <Input type="select" name="tipo" value={nuevoUser.tipo} onChange={handleInputChange}>
                  <option value="">Seleccione...</option>
                  <option value="admin">Administrador</option>
                  <option value="operator">Operador</option>
                  
                </Input>
              </FormGroup>
              <FormGroup>
                <Label for="password">Contraseña</Label>
                <Input type="text" name="password" placeholder='Ingrese una nueva contrasena' onChange={handleInputChange} />
              </FormGroup>

            </Col>

            
          </Row>
          <div className="d-flex justify-content-center mt-4">
            <Button className={ `${s.nBotonRecetas} mr-2`} onClick={handleSubmit}>
              {modoEditar ? 'Guardar Cambios' : 'Guardar'}
            </Button>
            <Button className={s.nBotonRecetas} onClick={onClose}>Cancelar</Button>
          </div>
          <div className='mb-5'></div>
          <hr></hr>
          <div className='mb-4'></div>
        </Col>
      </Row>
    </div>
  );
};

export default NuevoUsuario;

  