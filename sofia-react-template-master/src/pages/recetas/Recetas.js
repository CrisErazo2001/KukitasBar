import React, { useState } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon } from 'reactstrap';
import NuevaReceta from './NuevaReceta'; // Importa el componente para crear/editar recetas
import Modal from 'react-modal'; // Para mostrar el popup de vista detallada
import s from "../ingredientes/Ingredientes.module.scss";
import SearchBarIcon from "../../components/Icons/HeaderIcons/SearchBarIcon";

Modal.setAppElement('#root'); // Asegúrate de añadir esto

const Recetas = () => {
  // Ingredientes predefinidos para que puedas usar en las recetas quemadas
  const ingredientesPorDefecto = [
    { nombre: 'Ron', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Vodka', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Tequila', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Whiskey', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Triple Sec', tipo: 'Alcohol', costo: '1.23', cantidad: '750' }
  ];

  // Recetas predeterminadas (quemadas)
  const recetasPorDefecto = [
    { nombre: 'Mojito', ingredientes: [ingredientesPorDefecto[0], ingredientesPorDefecto[1]] },
    { nombre: 'Piña Colada', ingredientes: [ingredientesPorDefecto[3], ingredientesPorDefecto[2]] },
  ];

  const [recetas, setRecetas] = useState(recetasPorDefecto); // Inicia con recetas predeterminadas
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
          ingredientes={ingredientesPorDefecto} // Ingredientes disponibles
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
                    {ing.nombre}{idx < receta.ingredientes.length - 1 ? ', ' : ''}
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
