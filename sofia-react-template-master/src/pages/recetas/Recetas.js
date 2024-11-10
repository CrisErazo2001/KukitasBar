import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon, Pagination, PaginationItem, PaginationLink  } from 'reactstrap';
import NuevaReceta from './NuevaReceta'; // Importa el componente para crear/editar recetas
import Modal from 'react-modal'; // Para mostrar el popup de vista detallada
import s from "../ingredientes/Ingredientes.module.scss";
import SearchBarIcon from "../../components/Icons/HeaderIcons/SearchBarIcon";
// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";

Modal.setAppElement('#root'); // Asegúrate de añadir esto

const Recetas = () => {
  //Config de Notificaciones
  const options = {
    autoClose: 3000,
    closeButton: false,
    hideProgressBar: true,
    position: toast.POSITION.TOP_CENTER,
  };
  const [ingredientes, setIngredientes] = useState([]);
  const [busqueda, setBusqueda] = useState('');
  const [mostrarFormulario, setMostrarFormulario] = useState(false);
  const [recetaSeleccionada, setRecetaSeleccionada] = useState(null);
  const [modoEditar, setModoEditar] = useState(false); // Modo para editar receta
  const [deleteRecStatus, setDeleteRecStatus] = useState({});
  const [toggleStatus, setToggleStatus] = useState({});
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

  
  const [recetas, setRecetas] = useState([]); // Inicia con recetas predeterminadas

  /* Nuevo */
  // Nuevo estado para almacenar el estado de "en menú" de cada receta.
  const [recetasEnMenu, setRecetasEnMenu] = useState({}); // Objeto que almacenará el estado para cada receta por ID
    // Función para alternar el estado de "en menú" de una receta específica.
  const toggleMenuStatus = (receta) => {

    fetch('/receta/toggleStatus', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(receta)
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setToggleStatus(data); // Guarda la respuesta en createIngStatus
        // setIngredientes((prevIngredientes) => [...prevIngredientes, nuevoIngrediente]);
    })
    .catch(error => console.error('Error:', error));
    
  };
  /* Nuevo */

  const fetchRecetas = async () => {
    try {
      const response = await fetch('/recetas'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched Recetas:', list.data); // Mostrar en consola la lista obtenida
      setRecetas(list.data); // Guardar la lista en el estado
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  


  

  // Filtrar las recetas según la búsqueda
  const filtrarRecetas = recetas.filter((receta) =>
    receta.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  // Función para abrir el formulario de edición
  const abrirFormularioEdicion = (receta) => {
    setModoEditar(true);
    setRecetaSeleccionada(receta);
    setMostrarFormulario(true);
    setMostrarTabla(false); // Ocultar tabla cuando se edita
  };

  // Función para eliminar una receta
  const eliminarReceta = (receta) => {
    fetch('/receta/eliminar', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(receta)
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setDeleteRecStatus(data); // Guarda la respuesta en createIngStatus
        // setIngredientes((prevIngredientes) => [...prevIngredientes, nuevoIngrediente]);
    })
    .catch(error => console.error('Error:', error));
  };
  useEffect(() => {
    console.log('Estado de deleteRecStatus:', deleteRecStatus);
    
    if (deleteRecStatus.code > 0){
      
      toast(
        
        <Notification 
            type={deleteRecStatus.status} 
            errorMessage={deleteRecStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [deleteRecStatus]);
  useEffect(() => {
    fetchIngredientes();
    fetchRecetas();
  }, [mostrarFormulario,deleteRecStatus,toggleStatus]);

  /* Nuevo */

  // Configuración de la paginación
  const indiceUltimoElemento = paginaActual * elementosPorPagina;
  const indicePrimerElemento = indiceUltimoElemento - elementosPorPagina;
  const ingredientesPaginados = filtrarRecetas.slice(indicePrimerElemento, indiceUltimoElemento);

  const cambiarPagina = (pagina) => setPaginaActual(pagina);
  const totalPaginas = Math.ceil(filtrarRecetas.length / elementosPorPagina);


  return (
    <div>
      <Row>
        <Col className="mb-4" xs={12}>
          <div className='mb-4' style={{backgroundColor:'#ebf5fa', padding:'20px'}}>
            <div className='d-flex flex-column justify-content-sm-center align-items-center'>
              <h5>Crear Nueva Receta</h5>
              <Button className={s.nBotonRecetas} onClick={() => {
                setMostrarFormulario(true); // Mostrar formulario de creación de recetas
                setModoEditar(false); // Modo crear, no editar
                setRecetaSeleccionada(null); // Limpia selección anterior
                setMostrarTabla(false); // p
              }}>
                Crear Nueva Receta
              </Button>
            </div>
            <div className="d-flex flex-column align-items-center justify-content-space-between mt-3">
              <h5 className='mr-4'>Mostrar Recetas</h5>
              <Button className={s.nBotonRecetas} onClick={() => {
                setMostrarTabla(true);
                setMostrarFormulario(false);
              }}>
                Mostrar Recetas
              </Button>
            </div>
          </div>
          {/* Formulario de creación/edición de receta */}
          {mostrarFormulario && (
            <NuevaReceta
              onClose={() => setMostrarFormulario(false)}
              setRecetas={setRecetas}
              recetas={recetas}
              ingredientes={ingredientes} // Ingredientes disponibles
              receta={recetaSeleccionada} // Receta seleccionada para edición
              modoEditar={modoEditar} // Modo edición
            />
          )}
        </Col>
      </Row>

      

      {mostrarTabla && (
      <div>
        {/* Buscador y botón */}
        <div className={s.boxbuscador}>
          <div className={s.searchContainer}>
            <InputGroup className="input-group-no-border search-input-group">
              <Input
                type="text"
                placeholder="Buscar Receta"
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
     

        {/* Tabla de recetas */}
        <Table responsive>
          <thead>
            <tr>
              <th>Nombre de la Receta</th>
              <th>Ingredientes</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {ingredientesPaginados.map((receta, index) => (
              <tr key={index}>
                <td>{receta.nombre}</td>
                <td>
                  {receta.ingredientes.map((ing, idx) => (
                    <span key={idx}>
                      {ing.nombre}{idx < receta.ingredientes.length - 1 ? ', ' : ''}
                    </span>
                  ))}
                </td>
                <td>
                  <div className='d-flex flex-column'>
                    <Button className={s.nBotonEdicion} onClick={() => abrirFormularioEdicion(receta)}>Editar</Button>
                    <div className='mb-3'></div>
                    <Button className={s.nBotonEdicion} onClick={() => eliminarReceta(receta)}>Eliminar</Button>
                    <div className='mb-3'></div>
                    <Button className={s.nBotonEdicion} onClick={() => toggleMenuStatus(receta)}>
                      {receta.menu ? 'Quitar del Menú' : 'Agregar al Menú'} {/* Texto dinámico */}
                    </Button>
                  </div>
                  {/* Nuevo botón para agregar/quitar del menú */}
                  

                  {/* Estado de la receta para visualización */}
                  <div style={{ marginTop: '10px', fontSize: '14px' }}>
                    La receta irá en el Menú: {receta.menu ? 'Verdadero' : 'Falso'}
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

    </div>
  );
};

export default Recetas;
