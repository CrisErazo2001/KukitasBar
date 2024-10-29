import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon } from 'reactstrap';
import NuevaReceta from './NuevaReceta'; // Importa el componente para crear/editar recetas
import Modal from 'react-modal'; // Para mostrar el popup de vista detallada
import s from "../ingredientes/Ingredientes.module.scss";
import SearchBarIcon from "../../components/Icons/HeaderIcons/SearchBarIcon";

Modal.setAppElement('#root'); // Asegúrate de añadir esto

const Recetas = () => {
  const [ingredientes, setIngredientes] = useState([]);

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

  useEffect(() => {
    fetchIngredientes();
    fetchRecetas();
  }, []);


  const [busqueda, setBusqueda] = useState('');
  const [mostrarFormulario, setMostrarFormulario] = useState(false);
  const [recetaSeleccionada, setRecetaSeleccionada] = useState(null);
  const [modoEditar, setModoEditar] = useState(false); // Modo para editar receta

  // Filtrar las recetas según la búsqueda
  const filtrarRecetas = recetas.filter((receta) =>
    receta.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  // Función para abrir el formulario de edición
  const abrirFormularioEdicion = (receta) => {
    setModoEditar(true);
    setRecetaSeleccionada(receta);
    setMostrarFormulario(true);
  };

  // Función para eliminar una receta
  const eliminarReceta = (receta) => {
    const nuevasRecetas = recetas.filter((rec) => rec !== receta);
    setRecetas(nuevasRecetas);
  };

  return (
    <div>
      <Row>
        <Col className="mb-4" xs={12}>
          {/* Buscador y botón */}
          <div className="d-flex align-items-center justify-content-end">
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
            <div>
              <Button className={s.nBotonRecetas} onClick={() => {
                setMostrarFormulario(true); // Mostrar formulario de creación de recetas
                setModoEditar(false); // Modo crear, no editar
                setRecetaSeleccionada(null); // Limpia selección anterior
              }}>
                Nueva Receta
              </Button>
            </div>
          </div>
        </Col>
      </Row>

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
          {filtrarRecetas.map((receta, index) => (
            <tr key={index}>
              <td>{receta.nombre}</td>
              <td>
                {receta.ingredientes.map((ing, idx) => (
                  <span key={idx}>
                    {ing}{idx < receta.ingredientes.length - 1 ? ', ' : ''}
                  </span>
                ))}
              </td>
              <td>
                <div className='d-flex flex-column'>
                  <Button className={s.nBotonEdicion} onClick={() => abrirFormularioEdicion(receta)}>Editar</Button>
                  <div className='mb-3'></div>
                  <Button className={s.nBotonEdicion} onClick={() => eliminarReceta(receta)}>Eliminar</Button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Recetas;
