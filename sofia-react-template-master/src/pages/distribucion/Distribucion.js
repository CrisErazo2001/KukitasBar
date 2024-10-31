import React, { useState, useEffect } from 'react';
import { Modal, ModalHeader, ModalBody, Button, Row, Col, Input, FormGroup, Label } from 'reactstrap';
import Select from 'react-select';
import s from './Distribucion.module.scss';

const Distribucion = () => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [botonSeleccionado, setBotonSeleccionado] = useState('');
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);
  const [nombreDisposicion, setNombreDisposicion] = useState('');
  const [ingredientes, setIngredientes] = useState([]);
  const [distribucionNombres, setDistribucionNombres] = useState([]);
  const [cantidades, setCantidades] = useState(Array.from({ length: 28 }, () => ({ cantidadActual: -1, cantidadUsada: 0 })));
  const [cambioIngrediente, setCambioIngrediente] = useState(Array.from({ length: 28 }, () => (false)));
  const [nombres, setNombres] = useState([]);
  const [distribucion, setDistribucion] = useState('');

  const fetchIngredientes = async () => {
    try {
      const response = await fetch('/ingredientes/nombres'); // Reemplaza con tu URL de API
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

  const fetchDistribucionNombres = async () => {
    try {
      const response = await fetch('/posiciones/nombres'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched Distribucion Nombres:', list.data); // Mostrar en consola la lista obtenida
      setNombres(list.data); // Guardar la lista en el estado
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
    console.log('ingrediente', ingrediente)
    setIngredienteSeleccionado(ingrediente);
  };

  const manejarCambioDistribucion = (distribucion) => {
      setDistribucion(distribucion); 
  };

  const rellenarCantidad = () => {
    
  };


  const guardarPosicion = () => {
    setDistribucionNombres((prev) => {
      const nuevaDistribucion = [...prev]; // Crear una copia de la lista anterior
      nuevaDistribucion[botonSeleccionado] = ingredienteSeleccionado.value; // Actualizar solo el índice deseado
      return nuevaDistribucion; // Retornar la lista actualizada
    });
    setCambioIngrediente((prev)=>{
      const nuevoCambio = [...prev];
      nuevoCambio[botonSeleccionado] = true;
      return nuevoCambio;
    })
    cerrarModal();
  };

  

  const borrarDisposicion = () => {
    
  };

  const rellenarTodasBotellas = () => {
    
  };

  const obtenerColorBoton = (boton) => {
    // console.log('boton #:',boton);
    const ingrediente  = distribucionNombres[boton];
    if (ingrediente == '') return '#d3d3d3'; // Gris cuando no hay selección
    if (cantidades[boton].cantidadActual < 30 && cantidades[boton].cantidadActual != -1) return '#ffd700'; // Amarillo cuando está vacío
    if (cambioIngrediente[boton] == true) return '#00FF28'; 
    return '#ff8b05'; // Naranja para los demás ingredientes
  };
  useEffect(()=>{
    
    fetch('/posicion/set', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({nombre: distribucion})
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setNombreDistribStatus(data); // Guarda la respuesta en createIngStatus
    })
    .catch(error => console.error('Error:', error));


  },[distribucion]);
  

  useEffect(() => {
    fetchIngredientes();
    fetchDistribucion();
    fetchCantidades();
    fetchDistribucionNombres();
  }, []);

  useEffect(()=>{
    console.log('cantidades',cantidades);
    console.log('posiciones',distribucionNombres);
  },[modalIsOpen]);

  return (
    <div>
      <div style={{width:"50%", position: 'absolute', top: 20, right: 20 }}>
        <Select 
          options={nombres} 
          placeholder="Seleccionar opción"
          onChange={(e) => setDistribucion(e.target.value)}
        />
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
        <div className={s.leyendaItem}>
          <span>Espacio Modificado</span>
          <div className={s.circuloLeyenda} style={{ backgroundColor: "#00ff28" }}></div>
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
                style={{ backgroundColor: obtenerColorBoton(27 - i) }}
                onClick={() => abrirModal(27 - i)}
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
                style={{ backgroundColor: obtenerColorBoton(20 - i) }}
                onClick={() => abrirModal(20 - i)}
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
              style={{ backgroundColor: obtenerColorBoton(13 - i) }}
              onClick={() => abrirModal(13 - i)}
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
              style={{ backgroundColor: obtenerColorBoton(6 - i) }}
              onClick={() => abrirModal(6 - i)}
              className={`${s.distribucionButton}`}
            >
              {`A${7 - i}`}
            </Button>
          ))}
        </div>
      </div>

      <div style={{ display: "flex", justifyContent: "center", marginTop: "20px" }}>
        <Input
          type="text"
          value={nombreDisposicion}
          onChange={(e) => setNombreDisposicion(e.target.value)}
          placeholder="Nombre de la disposición"
        />
      </div>
      <div style={{ display: "flex", justifyContent: "center", marginTop: "20px" }}>
        <Button className={s.nBotonRecetas} onClick={guardarDisposicion}>Guardar Disposición</Button>
        <Button className={s.nBotonRecetas} onClick={rellenarTodasBotellas}>Rellenar Todo</Button>
        <Button className={s.nBotonRecetas} onClick={borrarDisposicion}>Borrar Todo</Button>
      </div>

      <Modal isOpen={modalIsOpen} toggle={cerrarModal}>
        <ModalHeader toggle={cerrarModal}>Configurar {botonSeleccionado}</ModalHeader>
        <ModalBody>
          
        <FormGroup>
            
            <Label for="ingrediente">Ingrediente</Label>
            <Select
              id="ingrediente"
              options={ingredientes}
              value={ingredienteSeleccionado}
              onChange={manejarCambioIngrediente}
              placeholder={distribucionNombres[botonSeleccionado] !== ''? distribucionNombres[botonSeleccionado]:"Seleccione un ingrediente"}
            />
          </FormGroup>
          
          
          <FormGroup>
            <Label for="cantidad">Cantidad Actual</Label>
            <Input
              type="number"
              id="cantidad"
              value={cantidades[botonSeleccionado]?.cantidadActual || 0}
              
              disabled = {true}
            />
          </FormGroup>
          <FormGroup>
            <Label for="cantidad">Cantidad Usada</Label>
            <Input
              type="number"
              id="cantidad"
              value={cantidades[botonSeleccionado]?.cantidadUsada||0}
              disabled = {true}
            />
          </FormGroup>
            
          
          
          <div style={{ display:"flex", justifyContent:"center", textAlign: 'center', margin: '30px 0' }}>
              <Button className={s.nBotonRecetas} onClick={rellenarCantidad}>Rellenar</Button>
          </div>
          <div style={{ display:"flex", justifyContent:"center", textAlign: 'center', margin: '10px 0' }}>
            <Button className={s.nBotonRecetas} onClick={guardarPosicion}>Guardar Posición</Button>
          </div>
        </ModalBody>
      </Modal>
    </div>
  );
};

export default Distribucion;
