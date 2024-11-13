import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon, ModalBody } from 'reactstrap';
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


  /* Nuevo Modal */

  /*nuevo Modal */
  /*nuevo Modal */
  const [showConfirmModal, setShowConfirmModal] = useState(false); // Estado para mostrar el modal de confirmación
  const [usuarioParaEliminar, setUsuarioParaEliminar] = useState(null); // Estado para la receta a eliminar

  // Mostrar el modal de confirmación
  const handleShowConfirmModal = (ingrediente) => {
    setUsuarioParaEliminar(ingrediente);
    setShowConfirmModal(true);
  };

  // Ocultar el modal de confirmación
  const handleCloseConfirmModal = () => {
    setShowConfirmModal(false);
    setUsuarioParaEliminar(null);
  };

  // Confirmar la eliminación
  const handleConfirmDelete = () => {
    eliminarIngrediente(usuarioParaEliminar);
    handleCloseConfirmModal(); // Cerrar el modal después de la eliminación
  };


  /* Nuevo Modal */

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
          <div className={s.boxbuscador}>
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
                  {/*
                  <Button className={s.nBotonEdicion} onClick={() => eliminarIngrediente(usuario)}>Eliminar</Button>
                  */}
                  <Button className={s.nBotonEdicion} onClick={() => handleShowConfirmModal(usuario)}>Eliminar</Button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>

      {/* Modal de confirmación para eliminar receta */}
      <Modal 
        isOpen={showConfirmModal} 
        toggle={handleCloseConfirmModal}
        onClick={(e) => {
          // Detecta si el clic fue fuera del modal
          if (e.target.classList.contains("modal")) {
            handleCloseConfirmModal();  // Cierra el modal si se hace clic fuera de él
          }
        }} 
        style={{
          overlay: { backgroundColor: 'rgba(255, 139, 5, 0.7)' },
          content: { maxWidth: '500px', maxHeight:'320px', margin: 'auto', padding: '20px', borderRadius: '10px' }
        }}
        
      >
        <ModalBody>
        <div className="d-flex flex-column justify-content-center">
          <h3 className="d-flex  justify-content-center align-content-center">
            Confirmar eliminación
          </h3>
          <p className="d-flex  justify-content-center mt-3">
            ¿Estás seguro de que deseas eliminar esta Usuario?
          </p>
          <div className='d-flex  justify-content-center mt-4' >
            <Button 
              color="danger" 
              onClick={handleConfirmDelete}
              className={s.nBotonEdicion}
            >
              Eliminar
            </Button>
            <Button 
              color="secondary" 
              onClick={handleCloseConfirmModal}
              className={s.nBotonEdicion}
            >
              Cancelar
            </Button>
          </div>
        </div>
        </ModalBody>
      </Modal>

      
    </div>
  );
};

export default Users;
