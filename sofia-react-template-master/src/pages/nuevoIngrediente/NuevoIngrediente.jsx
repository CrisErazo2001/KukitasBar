import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Input, FormGroup, Label } from 'reactstrap';
import s from "../ingredientes/Ingredientes.module.scss";

{/* 
const NuevoIngrediente = ({ onClose, setIngredientes }) => {
  const [nuevoIngrediente, setNuevoIngrediente] = useState({
    nombre: '',
    tipo: '',
    stockNumber: 0,
    descripcion: '',
    cantidad: 750,
    costo: 0,
    proveedor: ''
  });
*/}

  {/*
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNuevoIngrediente({ ...nuevoIngrediente, [name]: value });
  };

  const handleSubmit = () => {
    // Lógica para guardar el nuevo ingrediente
    setIngredientes((prevIngredientes) => [...prevIngredientes, nuevoIngrediente]);
    onClose();
  };
  */}

const NuevoIngrediente = ({ onClose, setIngredientes, ingredientes, ingrediente, modoEditar }) => {
  const [nuevoIngrediente, setNuevoIngrediente] = useState({
    nombre: '',
    tipo: '',
    stockNumber: 0,
    descripcion: '',
    cantidad: 750,
    costo: 0,
    proveedor: ''
  });

  // **Nuevo**: Cargar datos del ingrediente en modo edición
  useEffect(() => {
    if (modoEditar && ingrediente) {
      setNuevoIngrediente({
        nombre: ingrediente.nombre,
        tipo: ingrediente.tipo,
        stockNumber: ingrediente.stockNumber,
        descripcion: ingrediente.descripcion,
        cantidad: ingrediente.cantidad,
        costo: ingrediente.costo,
        proveedor: ingrediente.proveedor
      });
    } else {
      // Limpiar los campos si es modo creación
      setNuevoIngrediente({
        nombre: '',
        tipo: '',
        stockNumber: 0,
        descripcion: '',
        cantidad: 750,
        costo: 0,
        proveedor: ''
      });
    }
  }, [ingrediente, modoEditar]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNuevoIngrediente({ ...nuevoIngrediente, [name]: value });
  };

  const handleSubmit = () => {
    if (modoEditar) {
      // **Nuevo**: Si estamos editando, actualizar el ingrediente
      const ingredientesActualizados = ingredientes.map((ing) =>
        ing === ingrediente ? nuevoIngrediente : ing
      );
      setIngredientes(ingredientesActualizados);
    } else {
      // Si estamos creando, agregar un nuevo ingrediente
      setIngredientes((prevIngredientes) => [...prevIngredientes, nuevoIngrediente]);
    }

    onClose(); // Cierra el formulario
  };


  return (
    <div>
      <Row>
        <Col>
          <h3>{modoEditar ? 'Editar Ingrediente' : 'Agregar Nuevo Ingrediente'}</h3> {/* Título dinámico */}
          <Row>
            <Col md={6}>
              <FormGroup>
                <Label for="nombre">Nombre del Ingrediente</Label>
                <Input
                  type="text"
                  name="nombre"
                  value={nuevoIngrediente.nombre}
                  onChange={handleInputChange}
                />
              </FormGroup>

              <FormGroup>
                <Label for="tipo">Categoría</Label>
                <Input type="select" name="tipo" value={nuevoIngrediente.tipo} onChange={handleInputChange}>
                  <option value="">Seleccione...</option>
                  <option value="Alcohol">Alcohol</option>
                  <option value="Soda">Soda</option>
                  <option value="Cerveza">Cerveza</option>
                </Input>
              </FormGroup>

              <FormGroup>
                <Label for="stockNumber">Stock Number</Label>
                <Input
                  type="number"
                  name="stockNumber"
                  value={nuevoIngrediente.stockNumber}
                  onChange={handleInputChange}
                />
              </FormGroup>

              <FormGroup>
                <Label for="descripcion">Descripción</Label>
                <Input
                  type="textarea"
                  name="descripcion"
                  value={nuevoIngrediente.descripcion}
                  onChange={handleInputChange}
                />
              </FormGroup>

              <FormGroup>
                <Label for="cantidad">Cantidad en Stock (cm3)</Label>
                <Input
                  type="select"
                  name="cantidad"
                  value={nuevoIngrediente.cantidad}
                  onChange={handleInputChange}
                >
                  <option value={750}>750</option>
                  <option value={1000}>1000</option>
                  <option value={1500}>1500</option>
                  <option value={2000}>2000</option>
                </Input>
              </FormGroup>
            </Col>

            <Col md={6}>
              <FormGroup>
                <Label for="costo">Costo por Unidad</Label>
                <Input
                  type="number"
                  name="costo"
                  step="0.01"
                  value={nuevoIngrediente.costo}
                  onChange={handleInputChange}
                />
              </FormGroup>

              <FormGroup>
                <Label for="proveedor">Proveedor</Label>
                <Input
                  type="text"
                  name="proveedor"
                  value={nuevoIngrediente.proveedor}
                  onChange={handleInputChange}
                />
              </FormGroup>
            </Col>
          </Row>
          <div className='mb-5'></div>
          {/* Botones */}
          <div className="d-flex justify-content-center">
            <Button className={s.nBotonRecetas} onClick={handleSubmit}>
              {modoEditar ? 'Guardar Cambios' : 'Guardar'}
            </Button>{' '}
            <Button className={s.nBotonRecetas} onClick={onClose}>Cancelar</Button>
          </div>
          <div className='mb-5'></div>
          <hr />
          <div className='mb-5'></div>
        </Col>
      </Row>
    </div>
  );
};

export default NuevoIngrediente;

  {/*
  return (
    <div>
      <Row>
        <Col>
          <h3>Agregar Nuevo Ingrediente</h3>
          <Row>
            <Col md={6}>
              <FormGroup>
                <Label for="nombre">Nombre del Ingrediente</Label>
                <Input
                  type="text"
                  name="nombre"
                  value={nuevoIngrediente.nombre}
                  onChange={handleInputChange}
                />
              </FormGroup>

              <FormGroup>
                <Label for="tipo">Categoría</Label>
                <Input type="select" name="tipo" value={nuevoIngrediente.tipo} onChange={handleInputChange}>
                  <option value="">Seleccione...</option>
                  <option value="Alcohol">Alcohol</option>
                  <option value="Soda">Soda</option>
                  <option value="Cerveza">Cerveza</option>
                </Input>
              </FormGroup>

              <FormGroup>
                <Label for="stockNumber">Stock Number</Label>
                <Input
                  type="number"
                  name="stockNumber"
                  value={nuevoIngrediente.stockNumber}
                  onChange={handleInputChange}
                />
              </FormGroup>

              <FormGroup>
                <Label for="descripcion">Descripción</Label>
                <Input
                  type="textarea"
                  name="descripcion"
                  value={nuevoIngrediente.descripcion}
                  onChange={handleInputChange}
                />
              </FormGroup>

              <FormGroup>
                <Label for="cantidad">Cantidad en Stock (cm3)</Label>
                <Input
                  type="select"
                  name="cantidad"
                  value={nuevoIngrediente.cantidad}
                  onChange={handleInputChange}
                >
                  <option value={750}>750</option>
                  <option value={1000}>1000</option>
                  <option value={1500}>1500</option>
                  <option value={2000}>2000</option>
                </Input>
              </FormGroup>
            </Col>

            <Col md={6}>
              <FormGroup>
                <Label for="costo">Costo por Unidad</Label>
                <Input
                  type="number"
                  name="costo"
                  step="0.01"
                  value={nuevoIngrediente.costo}
                  onChange={handleInputChange}
                />
              </FormGroup>

              <FormGroup>
                <Label for="proveedor">Proveedor</Label>
                <Input
                  type="text"
                  name="proveedor"
                  value={nuevoIngrediente.proveedor}
                  onChange={handleInputChange}
                />
              </FormGroup>
            </Col>
          </Row>
          <div className='mb-5'></div>
          
          <div className="d-flex justify-content-center">
            <Button className={s.nBotonRecetas} onClick={handleSubmit}>Guardar</Button>{' '}
            <Button className={s.nBotonRecetas}  onClick={onClose}>Cancelar</Button>
          </div>
          <div className='mb-5'></div>
          <hr />
          <div className='mb-5'></div>
          
        </Col>
      </Row>
    </div>
  );
};

export default NuevoIngrediente;

*/}