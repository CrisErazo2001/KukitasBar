import React, { useState } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon} from 'reactstrap';
import NuevoIngrediente from '../nuevoIngrediente/NuevoIngrediente'; // Importa el componente para agregar ingredientes
import Modal from 'react-modal'; // Para mostrar el popup de vista detallada
import s from "./Ingredientes.module.scss";
import SearchBarIcon from "../../components/Icons/HeaderIcons/SearchBarIcon"

Modal.setAppElement('#root'); // Asegúrate de añadir esto


const Ingredientes = () => {

  const ingredientesPorDefecto = [
    { nombre: 'Ron', tipo: 'Alcohol', costo: '1.20', cantidad: '750' },
    { nombre: 'Vodka', tipo: 'Alcohol', costo: '1.20', cantidad: '750' },
    { nombre: 'Whiskey', tipo: 'Alcohol', costo: '1.20', cantidad: '750' }
  ];

  const [ingredientes, setIngredientes] = useState(ingredientesPorDefecto); // Inicia con ingredientes predeterminados
  // const [ingredientes, setIngredientes] = useState([]); // Aquí deberás cargar la lista de ingredientes
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);
  const [busqueda, setBusqueda] = useState('');
  const [mostrarFormulario, setMostrarFormulario] = useState(false);
  const [modoEditar, setModoEditar] = useState(false); // **Nuevo**: Define si se está editando

  // Manejo de búsqueda de ingredientes
  const filtrarIngredientes = ingredientes.filter((ingrediente) =>
    ingrediente.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  // Abrir el modal de visualización
  const abrirModal = (ingrediente) => {
    setIngredienteSeleccionado(ingrediente);
    setModalIsOpen(true);
  };

  // Cerrar modal
  const cerrarModal = () => {
    setModalIsOpen(false);
    setIngredienteSeleccionado(null);
  };

  // **Nuevo**: Función para abrir el formulario de edición
  const abrirFormularioEdicion = (ingrediente) => {
    setModoEditar(true); // Activa el modo edición
    setIngredienteSeleccionado(ingrediente); // Asigna el ingrediente a editar
    setMostrarFormulario(true); // Muestra el formulario
  };

  // **Nuevo**: Función para eliminar un ingrediente
  const eliminarIngrediente = (ingrediente) => {
    const nuevosIngredientes = ingredientes.filter((ing) => ing !== ingrediente);
    setIngredientes(nuevosIngredientes);
  };

  return (
    <div>
      <Row>
        <Col className="mb-4" xs={12}>


          {/* Buscador y botón */}
          <div className="d-flex align-items-center justify-content-end  ">
            
             {/* 
            <InputGroup InputGroup className='input-group-no-border'>
              <Input
                type="text"
                placeholder="Buscar Ingrediente"
                value={busqueda}
                onChange={(e) => setBusqueda(e.target.value)}
              />
              <InputGroupAddon addonType="prepend">
                <span>
                  <SearchBarIcon/>
                </span>
              </InputGroupAddon>
            </InputGroup>

            */}

            <div className={s.searchContainer}>
              <InputGroup className="input-group-no-border search-input-group">
                <Input
                  type="text"
                  placeholder="Buscar Ingrediente"
                  value={busqueda}
                  onChange={(e) => setBusqueda(e.target.value)}
                  readonly
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
              {/*
              <Button
                className={s.nBotonRecetas} 
                onClick={() => setMostrarFormulario(true)}>
                Nuevo Ingrediente
              </Button>
              */}
              <Button className={s.nBotonRecetas} onClick={() => {
                setMostrarFormulario(true); // Mostrar formulario
                setModoEditar(false); // **Nuevo**: No es edición, es creación
                setIngredienteSeleccionado(null); // **Nuevo**: Limpia selección anterior
              }}>
                Nuevo Ingrediente
              </Button>

            </div>

          </div>
        </Col>
      </Row>

      {/* Formulario para crear nuevo ingrediente 
      {mostrarFormulario && (
        <NuevoIngrediente onClose={() => setMostrarFormulario(false)} setIngredientes={setIngredientes} />
      )}
      */}

      {/* Formulario de creación/edición de ingrediente */}
      {mostrarFormulario && (
        <NuevoIngrediente
          onClose={() => setMostrarFormulario(false)}
          setIngredientes={setIngredientes}
          ingredientes={ingredientes}
          ingrediente={ingredienteSeleccionado} // **Nuevo**: Ingrediente seleccionado para edición
          modoEditar={modoEditar} // **Nuevo**: Modo edición
        />
      )}

      {/* Tabla de ingredientes */}
      <Table responsive>
        <thead>
          <tr>
            <th>Nombre del Ingrediente</th>
            <th>Tipo de Ingrediente</th>
            <th>Costo</th>
            <th>Cantidad por Unidad</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {filtrarIngredientes.map((ingrediente, index) => (
            <tr key={index}>
              <td>{ingrediente.nombre}</td>
              <td>{ingrediente.tipo}</td>
              <td>{ingrediente.costo}</td>
              <td>{ingrediente.cantidad}</td>
              {/*
              <td>
                <div className='d-flex flex-column'>
                  <Button className={s.nBotonRecetas} color="info" onClick={() => abrirModal(ingrediente)}>Ver</Button>{' '}
                  <div className='mb-3'></div>
                  <Button className={s.nBotonRecetas} color="warning">Editar</Button>{' '}
                  <div className='mb-3'></div>
                  <Button className={s.nBotonRecetas} color="danger">Eliminar</Button>
                </div>
              </td>
              */}
              <td>
                <div className='d-flex flex-column'>
                  {/* Botón para ver detalles */}
                  <Button className={s.nBotonEdicion} onClick={() => abrirModal(ingrediente)}>Ver</Button>{' '}
                  <div className='mb-3'></div>
                  {/* **Nuevo**: Botón para editar ingrediente */}
                  <Button className={s.nBotonEdicion} onClick={() => abrirFormularioEdicion(ingrediente)}>Editar</Button>{' '}
                  <div className='mb-3'></div>
                  {/* **Nuevo**: Botón para eliminar ingrediente */}
                  <Button className={s.nBotonEdicion} onClick={() => eliminarIngrediente(ingrediente)}>Eliminar</Button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>

      {/* Modal para ver detalles */}
      <Modal isOpen={modalIsOpen} onRequestClose={cerrarModal}>
        {ingredienteSeleccionado && (
          <div>
            <h2>{ingredienteSeleccionado.nombre}</h2>
            <p>Tipo: {ingredienteSeleccionado.tipo}</p>
            <p>Costo: {ingredienteSeleccionado.costo}</p>
            <p>Cantidad por Unidad: {ingredienteSeleccionado.cantidad}</p>
            <Button onClick={cerrarModal}>Cerrar</Button>
          </div>
        )}
      </Modal>
      
    </div>
  );
};

export default Ingredientes;
