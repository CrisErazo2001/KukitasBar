import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon } from 'reactstrap';
import NuevoIngrediente from './ModUsers.jsx';
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

  const [ingredientes, setIngredientes] = useState([]);
  const [deleteIngStatus, setDeleteIngStatus] = useState({});
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);
  const [busqueda, setBusqueda] = useState('');
  const [mostrarFormulario, setMostrarFormulario] = useState(false);
  const [modoEditar, setModoEditar] = useState(false);

  const fetchIngredientes = async () => {
    try {
      const response = await fetch('/ingredientes'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched Ingredients:', list.data); // Mostrar en consola la lista obtenida
      setIngredientes(list.data); // Guardar la lista en el estado
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  
  

  const filtrarIngredientes = ingredientes.filter((ingrediente) =>
    ingrediente.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  const abrirModal = (ingrediente) => {
    setIngredienteSeleccionado(ingrediente);
    setModalIsOpen(true);
  };

  const cerrarModal = () => {
    setModalIsOpen(false);
    setIngredienteSeleccionado(null);
  };

  const abrirFormularioEdicion = (ingrediente) => {
    setModoEditar(true);
    setIngredienteSeleccionado(ingrediente);
    setMostrarFormulario(true);
  };

  const eliminarIngrediente = (ingrediente) => {
    fetch('/ingrediente/eliminar', {
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
        setDeleteIngStatus(data); // Guarda la respuesta en createIngStatus
        // setIngredientes((prevIngredientes) => [...prevIngredientes, nuevoIngrediente]);
    })
    .catch(error => console.error('Error:', error));
  };

  useEffect(() => {
    fetchIngredientes();
  }, [mostrarFormulario,deleteIngStatus]);


  useEffect(() => {
    console.log('Estado de deleteIngStatus:', deleteIngStatus);
    
    if (deleteIngStatus.code == 200){
      
      toast(
        
        <Notification 
            type={'success'} 
            errorMessage={deleteIngStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }else if (deleteIngStatus.code == 400){
      toast(
        
        <Notification 
            type={'error'} 
            errorMessage={deleteIngStatus.message} 
            withIcon 
        />, 
        options
      );
    } 
  }, [deleteIngStatus]);

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
        <NuevoIngrediente
          onClose={() => setMostrarFormulario(false)}
          setIngredientes={setIngredientes}
          ingredientes={ingredientes}
          ingrediente={ingredienteSeleccionado}
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
          {filtrarIngredientes.map((ingrediente, index) => (
            <tr key={index}>
              <td>{ingrediente.nombre}</td>
              <td>{ingrediente.tipo}</td>
              <td>{ingrediente.costo}</td>
              <td>
                <div className='d-flex flex-column'>
                  <Button className={`${s.nBotonEdicion} mb-2`} onClick={() => abrirFormularioEdicion(ingrediente)}>Editar</Button>
                  <Button className={s.nBotonEdicion} onClick={() => eliminarIngrediente(ingrediente)}>Eliminar</Button>
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
