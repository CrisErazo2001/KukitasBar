import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon, Pagination, PaginationItem, PaginationLink } from 'reactstrap';
import NuevoIngrediente from '../nuevoIngrediente/NuevoIngrediente';
import Modal from 'react-modal';
import s from "./Ingredientes.module.scss";
import SearchBarIcon from "../../components/Icons/HeaderIcons/SearchBarIcon";
// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";



Modal.setAppElement('#root');

const Ingredientes = () => {
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
  // N
  const [mostrarTabla, setMostrarTabla] = useState(false); // Estado para la tabla

  // Estado para la paginación
  const [paginaActual, setPaginaActual] = useState(1);
  const elementosPorPagina = 6; // Cambia este número según la cantidad de elementos que desees mostrar por página

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
    setMostrarTabla(false); // Ocultar tabla cuando se edita
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
    
    if (deleteIngStatus.code > 0){
      
      toast(
        
        <Notification 
            type={deleteIngStatus.status} 
            errorMessage={deleteIngStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [deleteIngStatus]);

  /* Nuevo */

    // Configuración de la paginación
    const indiceUltimoElemento = paginaActual * elementosPorPagina;
    const indicePrimerElemento = indiceUltimoElemento - elementosPorPagina;
    const ingredientesPaginados = filtrarIngredientes.slice(indicePrimerElemento, indiceUltimoElemento);
  
    const cambiarPagina = (pagina) => setPaginaActual(pagina);
    const totalPaginas = Math.ceil(filtrarIngredientes.length / elementosPorPagina);

  return (
    <div>
    <Row>
    <Col className="mb-4" xs={12}>
      <div className="d-flex flex-column align-items-center justify-content-space-between">
        <h5 className='mr-4'>Crear Nuevo Ingrediente</h5>
        <Button className={s.nBotonRecetas} onClick={() => {
          setMostrarFormulario(true);
          setModoEditar(false);
          setIngredienteSeleccionado(null);
          setMostrarTabla(false); // p
        }}>
          Nuevo Ingrediente
        </Button>
      </div>
      <div className="d-flex flex-column align-items-center justify-content-space-between mt-3">
        <h5 className='mr-4'>Mostrar Ingredientes</h5>
        <Button className={s.nBotonRecetas} onClick={() => {
          setMostrarTabla(true);
          setMostrarFormulario(false);
        }}>
          Mostrar Ingredientes
        </Button>
      </div>
      {mostrarFormulario && (
        <NuevoIngrediente
          onClose={() => setMostrarFormulario(false)}
          setIngredientes={setIngredientes}
          ingredientes={ingredientes}
          ingrediente={ingredienteSeleccionado}
          modoEditar={modoEditar}
        />
      )}
    </Col>
  </Row>

  {mostrarTabla && (
  <div>
    <div className={s.boxbuscador}>
      <div className={s.searchContainer}>
        <InputGroup className="input-group-no-border search-input-group">
          <Input
            type="text"
            placeholder="Buscar Ingrediente"
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

    <Table responsive>
      <thead>
        <tr>
          <th>Nombre del Ingrediente</th>
          <th>Tipo</th>
          <th>Costo C/U</th>
          <th>Cantidad C/U</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        {ingredientesPaginados.map((ingrediente, index) => (
          <tr key={index}>
            <td>{ingrediente.nombre}</td>
            <td>{ingrediente.tipo}</td>
            <td>{ingrediente.costo}</td>
            <td>{ingrediente.cantidad}</td>
            <td>
              <div className='d-flex flex-column'>
                <Button className={`${s.nBotonEdicion} mb-2`} onClick={() => abrirModal(ingrediente)}>Ver</Button>
                <Button className={`${s.nBotonEdicion} mb-2`} onClick={() => abrirFormularioEdicion(ingrediente)}>Editar</Button>
                <Button className={s.nBotonEdicion} onClick={() => eliminarIngrediente(ingrediente)}>Eliminar</Button>
              </div>
            </td>
          </tr>
        ))}
      </tbody>
    </Table>

    {/* Paginación */}
    <Pagination className="d-flex justify-content-center">
      <PaginationItem disabled={paginaActual === 1}>
        <PaginationLink first onClick={() => cambiarPagina(1)} />
      </PaginationItem>
      <PaginationItem disabled={paginaActual === 1}>
        <PaginationLink previous onClick={() => cambiarPagina(paginaActual - 1)} />
      </PaginationItem>
      {[...Array(totalPaginas)].map((_, index) => (
        <PaginationItem active={paginaActual === index + 1} key={index}>
          <PaginationLink onClick={() => cambiarPagina(index + 1)}>
            {index + 1}
          </PaginationLink>
        </PaginationItem>
      ))}
      <PaginationItem disabled={paginaActual === totalPaginas}>
        <PaginationLink next onClick={() => cambiarPagina(paginaActual + 1)} />
      </PaginationItem>
      <PaginationItem disabled={paginaActual === totalPaginas}>
        <PaginationLink last onClick={() => cambiarPagina(totalPaginas)} />
      </PaginationItem>
    </Pagination>
  </div>
  )}



      <Modal 
        isOpen={modalIsOpen} 
        onRequestClose={cerrarModal}
        style={{
          overlay: { backgroundColor: 'rgba(255, 139, 5, 0.7)' },
          content: { maxWidth: '500px', margin: 'auto', padding: '20px', borderRadius: '10px', textAlign: 'left' }
        }}
      >
        {ingredienteSeleccionado && (
          <div className={s.modalContent}>
            {/* Botón de cierre en la esquina superior */}
            <button className={s.closeButton} onClick={cerrarModal}>&times;</button>

            {/* Título */}
            <h3 className={s.modalTitle}>Detalle del Ingrediente</h3>
            <hr />

            {/* Contenedor estilo tabla para dos columnas */}
            <div className={s.ingredienteTabla}>
              <div className={s.ingredienteFila}>
                <p className={s.label}>Ingrediente:</p>
                <span className={s.infoBox}>{ingredienteSeleccionado.nombre}</span>
              </div>
              <div className={s.ingredienteFila}>
                <p className={s.label}>Tipo:</p>
                <span className={s.infoBox}>{ingredienteSeleccionado.tipo}</span>
              </div>
              <div className={s.ingredienteFila}>
                <p className={s.label}>Costo:</p>
                <span className={s.infoBox}>{ingredienteSeleccionado.costo}</span>
              </div>
              <div className={s.ingredienteFila}>
                <p className={s.label}>Cantidad:</p>
                <span className={s.infoBox}>{ingredienteSeleccionado.cantidad} cm³</span>
              </div>
              <div className={s.ingredienteFila}>
                <p className={s.label}>Stock:</p>
                <span className={s.infoBox}>{ingredienteSeleccionado.stockNumber}</span>
              </div>
              <div className={s.ingredienteFila}>
                <p className={s.label}>Proveedor:</p>
                <span className={s.infoBox}>{ingredienteSeleccionado.proveedor}</span>
              </div>
              <div className={s.ingredienteFila}>
                <p className={s.label}>Descripción:</p>
                <span className={`${s.infoBox} ${s.descriptionBox}`}>{ingredienteSeleccionado.descripcion}</span>
              </div>
            </div>
          </div>
        )}
      </Modal>

    </div>
  );
};

export default Ingredientes;
