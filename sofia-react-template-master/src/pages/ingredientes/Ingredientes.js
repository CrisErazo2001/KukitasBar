import React, { useState } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon} from 'reactstrap';
import NuevoIngrediente from '../nuevoIngrediente/NuevoIngrediente'; // Importa el componente para agregar ingredientes
import Modal from 'react-modal'; // Para mostrar el popup de vista detallada
import s from "./Ingredientes.module.scss";
import SearchBarIcon from "../../components/Icons/HeaderIcons/SearchBarIcon"



const Ingredientes = () => {
  const [ingredientes, setIngredientes] = useState([]); // Aquí deberás cargar la lista de ingredientes
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);
  const [busqueda, setBusqueda] = useState('');
  const [mostrarFormulario, setMostrarFormulario] = useState(false);

  // Manejo de búsqueda de ingredientes
  const filtrarIngredientes = ingredientes.filter((ingrediente) =>
    ingrediente.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  // Abrir el modal de visualización
  const abrirModal = (ingrediente) => {
    setIngredienteSeleccionado(ingrediente);
    setModalIsOpen(true);
  };

  const cerrarModal = () => {
    setModalIsOpen(false);
    setIngredienteSeleccionado(null);
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
                  className={s.searchInput}
                />
                <InputGroupAddon addonType="prepend">
                  <span className={s.searchIcon}>
                    <SearchBarIcon />
                  </span>
                </InputGroupAddon>
              </InputGroup>
            </div>

            <Button 
              className={s.nBotonRecetas}
              onClick={() => setMostrarFormulario(true)}>
              Nuevo Ingrediente
            </Button>
            

          </div>
        </Col>
      </Row>

      {/* Formulario para crear nuevo ingrediente */}
      {mostrarFormulario && (
        <NuevoIngrediente onClose={() => setMostrarFormulario(false)} setIngredientes={setIngredientes} />
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
              <td>
                <Button color="info" onClick={() => abrirModal(ingrediente)}>Ver</Button>{' '}
                <Button color="warning">Editar</Button>{' '}
                <Button color="danger">Eliminar</Button>
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
