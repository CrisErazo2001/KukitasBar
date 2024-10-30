import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon } from 'reactstrap';
import NuevoUsuario from './ModUsers.jsx';
import Modal from 'react-modal';
import s from "./Users.module.scss";
import SearchBarIcon from "../../components/Icons/HeaderIcons/SearchBarIcon.js";
// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";



Modal.setAppElement('#root');

const Users = () => {
  //Config de Notificaciones
  const options = {
    autoClose: 3000,
    closeButton: false,
    hideProgressBar: true,
    position: toast.POSITION.TOP_CENTER,
  };

  const [usuarios, setUsuarios] = useState([]);
  const [deleteUserStatus, setDeleteUserStatus] = useState({});
  const [usuarioSeleccionado, setUsuarioSeleccionado] = useState(null);
  const [busqueda, setBusqueda] = useState('');
  const [mostrarFormulario, setMostrarFormulario] = useState(false);
  const [modoEditar, setModoEditar] = useState(false);

  const fetchUsuarios = async () => {
    try {
      const response = await fetch('/usuarios'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched Ingredients:', list.data); // Mostrar en consola la lista obtenida
      setUsuarios(list.data); // Guardar la lista en el estado
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  
  

  const filtrarUsuarios = usuarios.filter((usuario) =>
    usuario.user.toLowerCase().includes(busqueda.toLowerCase())
  );


  const abrirFormularioEdicion = (ingrediente) => {
    setModoEditar(true);
    setUsuarioSeleccionado(ingrediente);
    setMostrarFormulario(true);
  };

  const eliminarIngrediente = (ingrediente) => {
    fetch('/usuario/eliminar', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(ingrediente)
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setDeleteUserStatus(data); // Guarda la respuesta en createIngStatus
        // setUsuarios((prevIngredientes) => [...prevIngredientes, nuevoIngrediente]);
    })
    .catch(error => console.error('Error:', error));
  };

  useEffect(() => {
    fetchUsuarios();
  }, [mostrarFormulario,deleteUserStatus]);


  useEffect(() => {
    console.log('Estado de deleteUserStatus:', deleteUserStatus);
    
    if (deleteUserStatus.code > 0){
      
      toast(
        
        <Notification 
            type={deleteUserStatus.status} 
            errorMessage={deleteUserStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [deleteUserStatus]);

  return (
    <div>
      <Row>
        <Col className="mb-4" xs={12}>
          <div className="d-flex align-items-center justify-content-end">
            <div className={s.searchContainer}>
              <InputGroup className="input-group-no-border search-input-group">
                <Input
                  type="text"
                  placeholder="Buscar Usuario"
                  value={busqueda}
                  onChange={(e) => setBusqueda(e.target.value)}
                  className={s.searchInput}
                />
                <InputGroupAddon addonType="prepend">
                  <span className={s.searchIcon}>
                    <SearchBarIcon />
                  </span>
                </InputGroupAddon>
              </InputGroup>
            </div>
            
          </div>
        </Col>
      </Row>

      {mostrarFormulario && (
        <NuevoUsuario 
          onClose={() => setMostrarFormulario(false)}
          setUsuarios={setUsuarios}
          usuarios={usuarios}
          usuario={usuarioSeleccionado}
          modoEditar={modoEditar}
        />
      )}

      <Table responsive>
        <thead>
          <tr>
            <th>Nombre del Usuario</th>
            <th>Tipo</th>
            <th>Creado el</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {filtrarUsuarios.map((usuario, index) => (
            <tr key={index}>
              <td>{usuario.user}</td>
              <td>{usuario.tipo}</td>
              <td>{usuario.created_at}</td>
              <td>
                <div className='d-flex flex-column'>
                  <Button className={`${s.nBotonEdicion} mb-2`} onClick={() => abrirFormularioEdicion(usuario)}>Editar</Button>
                  <Button className={s.nBotonEdicion} onClick={() => eliminarIngrediente(usuario)}>Eliminar</Button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>

      
    </div>
  );
};

export default Users;
