import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Input, FormGroup, Label } from 'reactstrap';
import s from "../ingredientes/Ingredientes.module.scss";
// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";


const NuevoIngrediente = ({ onClose, setIngredientes, ingredientes, ingrediente, modoEditar }) => {
  //Config de Notificaciones
  const options = {
    autoClose: 3000,
    closeButton: false,
    hideProgressBar: true,
    position: toast.POSITION.TOP_CENTER,
  };
  const [createIngStatus, setCreateIngStatus] = useState({});
  const [modifyIngStatus, setModifyIngStatus] = useState({});
  const [nuevoIngrediente, setNuevoIngrediente] = useState({
    nombre: '',
    tipo: '',
    stockNumber: 0,
    descripcion: '',
    cantidad: 750,
    costo: 0,
    proveedor: ''
  });

  useEffect(() => {
    if (modoEditar && ingrediente) {
      setNuevoIngrediente(ingrediente);
    } else {
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
      fetch('/ingrediente/modificar', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(nuevoIngrediente)
      })
      .then(response => {
          console.log('Respuesta del servidor:', response); // Log de la respuesta
          return response.json();
      })
      .then(data => {
          console.log('Datos recibidos:', data); // Log de los datos recibidos
          setModifyIngStatus(data); // Guarda la respuesta en createIngStatus
          // setIngredientes((prevIngredientes) => [...prevIngredientes, nuevoIngrediente]);
          onClose(); // Llamar a onClose() solo después de recibir la respuesta del servidor
      })
      .catch(error => console.error('Error:', error));
      
    } else {
        fetch('/ingrediente/nuevo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(nuevoIngrediente)
        })
        .then(response => {
            console.log('Respuesta del servidor:', response); // Log de la respuesta
            return response.json();
        })
        .then(data => {
            console.log('Datos recibidos:', data); // Log de los datos recibidos
            setCreateIngStatus(data); // Guarda la respuesta en createIngStatus
            // setIngredientes((prevIngredientes) => [...prevIngredientes, nuevoIngrediente]);
            onClose(); // Llamar a onClose() solo después de recibir la respuesta del servidor
        })
        .catch(error => console.error('Error:', error));
    }
  };

  useEffect(() => {
      console.log('Estado de modifyIngStatus:', modifyIngStatus);
      
      if (modifyIngStatus.code > 0){
        
        toast(
          
          <Notification 
              type={modifyIngStatus.status} 
              errorMessage={modifyIngStatus.message} 
              withIcon 
          />, 
          options
        );
        
      }
  }, [modifyIngStatus]);
  useEffect(() => {
    console.log('Estado de createIngStatus:', createIngStatus);
    
    if (createIngStatus.code > 0){
      
      toast(
        
        <Notification 
            type={createIngStatus.status} 
            errorMessage={createIngStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
}, [createIngStatus]);

  return (
    <div style={{marginTop:'50px', borderTop:'1px solid #c4cbcf', paddingTop:'20px'}}>
      <Row>
        <Col>
          <h3>{modoEditar ? 'Editar Ingrediente' : 'Agregar Nuevo Ingrediente'}</h3>
          <Row>
            <Col md={6}>
              <FormGroup>
                <Label for="nombre">Nombre del Ingrediente</Label>
                <Input type="text" name="nombre" value={nuevoIngrediente.nombre} onChange={handleInputChange} />
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
                {/* <Label for="stockNumber">Stock Number</Label> */}
                <Input type="hidden" name="stockNumber" value={nuevoIngrediente.stockNumber} onChange={handleInputChange} readOnly={modoEditar}/>
              </FormGroup>
              <FormGroup>
                <Label for="descripcion">Descripción</Label>
                <Input type="textarea" name="descripcion" value={nuevoIngrediente.descripcion} onChange={handleInputChange} />
              </FormGroup>
              <FormGroup>
                <Label for="cantidad">Volumen de la botella (cm3)</Label>
                <Input type="select" name="cantidad" value={nuevoIngrediente.cantidad} onChange={handleInputChange}>
                  <option value={750}>750</option>
                  <option value={1000}>1000</option>
                  <option value={1500}>1500</option>
                  <option value={2000}>2000</option>
                </Input>
              </FormGroup>
            </Col>
            <Col md={6}>
              <FormGroup>
                <Label for="costo">Costo por botella ($)</Label>
                <Input type="number" name="costo" step="0.01" value={nuevoIngrediente.costo} onChange={handleInputChange} />
              </FormGroup>
              <FormGroup>
                <Label for="proveedor">Proveedor</Label>
                <Input type="text" name="proveedor" value={nuevoIngrediente.proveedor} onChange={handleInputChange} />
              </FormGroup>
            </Col>
          </Row>
          <div className="d-flex justify-content-center mt-4">
            <Button className={ `${s.nBotonRecetas} mr-2`} onClick={handleSubmit}>
              {modoEditar ? 'Guardar Cambios' : 'Guardar'}
            </Button>
            <Button className={s.nBotonRecetas} onClick={onClose}>Cancelar</Button>
          </div>
          <div className='mb-5'></div>
          <hr></hr>
          <div className='mb-5'></div>
        </Col>
      </Row>
    </div>
  );
};

export default NuevoIngrediente;

  