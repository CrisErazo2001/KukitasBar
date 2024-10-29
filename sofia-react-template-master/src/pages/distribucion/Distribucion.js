import React, { useState, useEffect } from 'react';
import { Modal, ModalHeader, ModalBody, Button, Row, Col, Input, FormGroup, Label } from 'reactstrap';
import Select from 'react-select';
import s from './Distribucion.module.scss';

const Distribucion = () => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [botonSeleccionado, setBotonSeleccionado] = useState('');
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);
  const [nombreDisposicion, setNombreDisposicion] = useState('');
  const [ingredientesNombres, setIngredientesNombres] = useState([]);
  const [distribucionNombres, setDistribucionNombres] = useState([]);
  const [cantidades, setCantidades] = useState(
    Array.from({ length: 28 }, (_, i) => ({
      cantidadActual: 750,
      cantidadUsada: 0,
      ingrediente: null
    })).reduce((acc, _, i) => {
      const fila = String.fromCharCode(65 + Math.floor(i / 7));
      const col = (i % 7) + 1;
      acc[`${fila}${col}`] = { cantidadActual: 750, cantidadUsada: 0, ingrediente: null };
      return acc;
    }, {})
  );
  
  const fetchIngredientes = async () => {
    try {
      const response = await fetch('/ingredientes'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched Ingredients:', list.data); // Mostrar en consola la lista obtenida
      const ingredientes = list.data
      const nombresFormateados = ingredientes.map((ingrediente) => ({
        value: ingrediente.nombre,
        label: ingrediente.nombre
      }));
      setIngredientesNombres(nombresFormateados);
      console.log('nombresFormateados',nombresFormateados);
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };
  const fetchDistribucion = async () => {
    try {
      const response = await fetch('/posiciones'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched Distribucion:', list.data); // Mostrar en consola la lista obtenida
      setDistribucionNombres(list.data); // Guardar la lista en el estado
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };
  const fetchCantidades = async () => {
    try {
      const response = await fetch('/cantidades'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched Cantidades:', list.data); // Mostrar en consola la lista obtenida
      setCantidades(list.data); // Guardar la lista en el estado
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  
  


  const abrirModal = (boton) => {
    setBotonSeleccionado(boton);
    setIngredienteSeleccionado(distribucionNombres[boton]);
    setModalIsOpen(true);
  };

  const cerrarModal = () => {
    setModalIsOpen(false);
  };

  const manejarCambioIngrediente = (ingrediente) => {
    setIngredienteSeleccionado(ingrediente);
  };

  const rellenarCantidad = () => {
    setCantidades((prev) => ({
      ...prev,
      [botonSeleccionado]: {
        ...prev[botonSeleccionado],
        cantidadUsada: prev[botonSeleccionado].cantidadActual
      }
    }));
  };

  const guardarPosicion = () => {
    setCantidades((prev) => ({
      ...prev,
      [botonSeleccionado]: {
        ...prev[botonSeleccionado],
        ingrediente: ingredienteSeleccionado
      }
    }));
    cerrarModal();
  };

  const guardarDisposicion = () => {
    console.log("Guardando disposición:", {
      nombre: nombreDisposicion,
      cantidades
    });
    // Aquí se podría agregar lógica para enviar la disposición a una API o almacenarla localmente.
  };

  const borrarDisposicion = () => {
    const cantidadesReseteadas = Object.keys(cantidades).reduce((acc, key) => {
      acc[key] = { ...cantidades[key], ingrediente: null, cantidadUsada: 0 };
      return acc;
    }, {});
    setCantidades(cantidadesReseteadas);
  };

  const rellenarTodasBotellas = () => {
    const cantidadesRellenadas = Object.keys(cantidades).reduce((acc, key) => {
      acc[key] = { ...cantidades[key], cantidadUsada: cantidades[key].cantidadActual };
      return acc;
    }, {});
    setCantidades(cantidadesRellenadas);
  };

  const obtenerColorBoton = (boton) => {
    
    const ingrediente  = distribucionNombres[boton-1];
    
    if (!ingrediente) return '#d3d3d3'; // Gris cuando no hay selección
    if (ingrediente.value === '') return '#ffd700'; // Amarillo cuando está vacío
    return '#ff8b05'; // Naranja para los demás ingredientes
  };
  
  const obtenerPosicion = (boton) => {
    
    const ingrediente  = distribucionNombres[boton-1];
  
    return ingrediente; 
  };
  

  useEffect(() => {
    fetchIngredientes();
    fetchDistribucion();
    fetchCantidades();
    
  }, []);

  return (
    <div>
      {/* Selector en la parte superior derecha */}
      
      <div style={{width:"50%", position: 'absolute', top: 20, right: 20 }}>
        {console.log('ingredientesNombres ',ingredientesNombres)}
        
        <Select options={ingredientesNombres} placeholder="Seleccionar opción" />
      </div>
      <div className={s.leyendaContainer}>
        <div className={s.leyendaItem}>
          <span>Espacio sin utilizar</span>
          <div className={s.circuloLeyenda} style={{ backgroundColor: "#d3d3d3" }}></div>
        </div>
        <div className={s.leyendaItem}>
          <span>Espacio vacío</span>
          <div className={s.circuloLeyenda} style={{ backgroundColor: "#FFFF00" }}></div>
        </div>
        <div className={s.leyendaItem}>
          <span>Espacio utilizado</span>
          <div className={s.circuloLeyenda} style={{ backgroundColor: "#ff8b05" }}></div>
        </div>
      </div>

      {/* Botonera */}
      <div className={s.botonera}>
        {/* Fila D y C */}
        <div className={s.filaVertical}>
          <div className={s.columnaVertical}>
            {Array.from({ length: 7 }, (_, i) => (
              <Button
                key={`D${7 - i}`}
                style={{ backgroundColor: obtenerColorBoton(21 + 7 - i) }}
                onClick={() => abrirModal(`D${7 - i}`)}
                className={`${s.distribucionButton}`}
              >
                {`D${7 - i}`}
              </Button>
            ))}
          </div>
          <div className={s.separadorVertical} />
          <div className={s.columnaVertical}>
            {Array.from({ length: 7 }, (_, i) => (
              <Button
                key={`C${7 - i}`}
                style={{ backgroundColor: obtenerColorBoton(14 + 7 - i) }}
                onClick={() => abrirModal(`C${7 - i}`)}
                className={`${s.distribucionButton}`}
              >
                {`C${7 - i}`}
              </Button>
            ))}
          </div>
        </div>
        
        {/* Fila B y A */}
        <div className={s.filaHorizontal}>
          {Array.from({ length: 7 }, (_, i) => (
            <Button
              key={`B${7 - i}`}
              style={{ backgroundColor: obtenerColorBoton(7 + 7 - i) }}
              onClick={() => abrirModal(`B${7 - i}`)}
              className={`${s.distribucionButton}`}
            >
              {`B${7 - i}`}
            </Button>
          ))}
        </div>

        <div className={s.separadorHorizontal} />

        <div className={s.filaHorizontal}>
          {Array.from({ length: 7 }, (_, i) => (
            <Button
              key={`A${7 - i}`}
              style={{ backgroundColor: obtenerColorBoton(7 - i) }}
              onClick={() => abrirModal(`A${7 - i}`)}
              className={`${s.distribucionButton}`}
            >
              {`A${7 - i}`}
            </Button>
          ))}
        </div>
      </div>

      {/* Modal */}
      <Modal isOpen={modalIsOpen} toggle={cerrarModal} centered className={`${s.modalCustom} overlayCustom`}>
        <ModalHeader className={s.modalHeader} toggle={cerrarModal}>
          <span className={s.modalTitle}>{botonSeleccionado}: {ingredienteSeleccionado?.label || 'Selecciona un ingrediente'}</span>
        </ModalHeader>
        <ModalBody className={s.modalBody}>
          <FormGroup>
            <Label for="ingredienteSelect">Nombre del Ingrediente</Label>
            <Select
              id="ingredienteSelect"
              value={ingredienteSeleccionado}
              onChange={manejarCambioIngrediente}
              options={ingredientesNombres}
              isSearchable
              placeholder="Selecciona un ingrediente"
              className={s.modalInput}
            />
          </FormGroup>

          <Row>
            <Col xs={6}>
              <FormGroup>
                <Label for="cantidadActual">Cantidad Actual</Label>
                <Input
                  type="number"
                  id="cantidadActual"
                  value={cantidades[botonSeleccionado]?.cantidadActual || 0}
                  readOnly
                />
              </FormGroup>
            </Col>
            <Col xs={6}>
              <FormGroup>
                <Label for="cantidadUsada">Cantidad Usada</Label>
                <Input
                  type="number"
                  id="cantidadUsada"
                  value={cantidades[botonSeleccionado]?.cantidadUsada || 0}
                  onChange={(e) => setCantidades((prev) => ({
                    ...prev,
                    [botonSeleccionado]: {
                      ...prev[botonSeleccionado],
                      cantidadUsada: parseFloat(e.target.value)
                    }
                  }))}
                />
              </FormGroup>
            </Col>
          </Row>

          <div style={{display:"flex", justifyContent:"center", textAlign: 'center', marginTop:"10px"}}> 
            <Button color="success" className={`${s.nBotonRecetas} mr-2`} onClick={rellenarCantidad}>
              Rellenar
            </Button>
            <Button color="primary" className={s.nBotonRecetas} onClick={guardarPosicion}>
              Guardar
            </Button>
          </div>
        </ModalBody>
      </Modal>

      {/* Input y Botón para Guardar Disposición */}
      <div style={{display:"flex", justifyContent:"center", textAlign: 'center', margin: '20px 0' }}>
        <Input
          type="text"
          placeholder="Nombre de la disposición"
          value={nombreDisposicion}
          onChange={(e) => setNombreDisposicion(e.target.value)}
          style={{ width: '300px', display: 'inline-block', marginRight: '10px' }}
        />
        <Button className={s.nBotonRecetas} onClick={guardarDisposicion} color="primary">
          Guardar Disposición
        </Button>
      </div>

      {/* Botones para Borrar y Rellenar Todas las Botellas */}
      <div style={{ display:"flex", justifyContent:"center", textAlign: 'center', margin: '10px 0' }}>
        <Button onClick={borrarDisposicion}  className={`${s.nBotonRecetas} mr-2`}>
          Borrar Disposición
        </Button>
        <Button className={s.nBotonRecetas} onClick={rellenarTodasBotellas} >
          Rellenar Todas las Botellas
        </Button>
      </div>
    </div>
  );
};

export default Distribucion;


