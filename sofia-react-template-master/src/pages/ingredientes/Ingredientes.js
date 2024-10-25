import React, { useState } from 'react';
import { Row, Col, Button, Table, Input, InputGroup, InputGroupAddon } from 'reactstrap';
import NuevoIngrediente from '../nuevoIngrediente/NuevoIngrediente';
import Modal from 'react-modal';
import s from "./Ingredientes.module.scss";
import SearchBarIcon from "../../components/Icons/HeaderIcons/SearchBarIcon";

Modal.setAppElement('#root');

const Ingredientes = () => {
  const ingredientesPorDefecto = [
    { nombre: 'Ron', tipo: 'Alcohol', costo: '1.20', cantidad: '750', stockNumber: 123, descripcion: 'Aged Rum', proveedor: 'ABC Suppliers' },
    { nombre: 'Vodka', tipo: 'Alcohol', costo: '1.20', cantidad: '750', stockNumber: 124, descripcion: 'Premium Vodka', proveedor: 'XYZ Distributors' },
    { nombre: 'Whiskey', tipo: 'Alcohol', costo: '1.20', cantidad: '750', stockNumber: 125, descripcion: 'Fine Whiskey', proveedor: 'Whiskey World' }
  ];

  const [ingredientes, setIngredientes] = useState(ingredientesPorDefecto);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);
  const [busqueda, setBusqueda] = useState('');
  const [mostrarFormulario, setMostrarFormulario] = useState(false);
  const [modoEditar, setModoEditar] = useState(false);

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
    const nuevosIngredientes = ingredientes.filter((ing) => ing !== ingrediente);
    setIngredientes(nuevosIngredientes);
  };

  return (
    <div>
      <Row>
        <Col className="mb-4" xs={12}>
          <div className="d-flex align-items-center justify-content-end">
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
            <Button className={s.nBotonRecetas} onClick={() => {
              setMostrarFormulario(true);
              setModoEditar(false);
              setIngredienteSeleccionado(null);
            }}>
              Nuevo Ingrediente
            </Button>
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
            <th>Nombre del Ingrediente</th>
            <th>Tipo</th>
            <th>Costo</th>
            <th>Cantidad</th>
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

      <Modal 
        isOpen={modalIsOpen} 
        onRequestClose={cerrarModal}
        style={{
          overlay: {
            backgroundColor: 'rgba(0, 0, 0, 0.5)'
          },
          content: {
            maxWidth: '500px',
            margin: 'auto',
            padding: '20px',
            borderRadius: '10px',
            textAlign: 'center'
          }
        }}
      >
        {ingredienteSeleccionado && (
          <div>

            <h2>Detalle de los ingredientes</h2>
            <hr></hr>
            <h2>{ingredienteSeleccionado.nombre}</h2>
            <p><strong>Tipo:</strong> {ingredienteSeleccionado.tipo}</p>
            <p><strong>Costo:</strong> {ingredienteSeleccionado.costo}</p>
            <p><strong>Cantidad:</strong> {ingredienteSeleccionado.cantidad} cm³</p>
            <p><strong>Stock Number:</strong> {ingredienteSeleccionado.stockNumber}</p>
            <p><strong>Descripción:</strong> {ingredienteSeleccionado.descripcion}</p>
            <p><strong>Proveedor:</strong> {ingredienteSeleccionado.proveedor}</p>
            <Button onClick={cerrarModal}>Cerrar</Button>
          </div>
        )}
      </Modal>
    </div>
  );
};

export default Ingredientes;
