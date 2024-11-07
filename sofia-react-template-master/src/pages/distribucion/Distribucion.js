import React, { useState, useEffect } from 'react';
import { Modal, ModalHeader, ModalBody, Button, Row, Col, Input, FormGroup, Label, InputGroup, InputGroupText } from 'reactstrap';
import Select from 'react-select';
import s from './Distribucion.module.scss';
// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";

const Distribucion = () => {

  //Config de Notificaciones
  const options = {
    autoClose: 3000,
    closeButton: false,
    hideProgressBar: true,
    position: toast.POSITION.TOP_CENTER,
  };

  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [botonSeleccionado, setBotonSeleccionado] = useState('');
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);
  const [nombreDisposicion, setNombreDisposicion] = useState('');
  const [ingredientes, setIngredientes] = useState(['']);
  const [distribucionNombres, setDistribucionNombres] = useState([]);
  const [cantidades, setCantidades] = useState(Array.from({ length: 28 }, () => ({ cantidadActual: -1, cantidadUsada: 0 })));
  const [cambioIngrediente, setCambioIngrediente] = useState(Array.from({ length: 28 }, () => (false)));
  const [nombres, setNombres] = useState([]);
  const [distribucion, setDistribucion] = useState('');
  const [nombreDistribStatus, setNombreDistribStatus] = useState({}); //seleccion de una distrib
  const [rellenarStatus,setRellenarStatus] = useState({});
  const [rellenarTodoStatus,setRellenarTodoStatus] = useState({});
  const [borrarStatus,setBorrarStatus] = useState({});
  const [guardarStatus,setGuardarStatus] = useState({});
  const [nombre,setNombre] = useState('');

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
      setNombre(list.nombre);
      // console.log('nombre', list.nombre)
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

  const manejarCambioDistribucion = (dis) => {
      console.log('distribucion',dis)
      setDistribucion(dis); 
  };

  const rellenarCantidad = () => {
    
    fetch('/cantidad/rellenar', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({pos: botonSeleccionado})
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setRellenarStatus(data); // Guarda la respuesta 
        
    })
    .catch(error => console.error('Error:', error));
    
    
  };


  const guardarPosicion = () => {
    
    if (ingredienteSeleccionado.value != ingredientes[botonSeleccionado]) {
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
    }
    
    cerrarModal();
  };

  const guardarDisposicion = () => {

    fetch('/posicion/save-distribucion', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({nombreSeleccionado: distribucion,nuevoNombre: nombreDisposicion, posiciones: distribucionNombres})
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setGuardarStatus(data); // Guarda la respuesta 
        
    })
    .catch(error => console.error('Error:', error));

    setCambioIngrediente(Array.from({ length: 28 }, () => (false)));
    setNombreDisposicion('');

  }
  

  const borrarDisposicion = () => {

    fetch('/posicion/borrar', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({nombreSeleccionado: distribucion,nuevoNombre: nombreDisposicion})
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setBorrarStatus(data); // Guarda la respuesta 
        
    })
    .catch(error => console.error('Error:', error));
    
  };

  const rellenarTodasBotellas = () => {

    fetch('/cantidad/rellenar-todo', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({cantidades: cantidades})
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setRellenarTodoStatus(data); // Guarda la respuesta 
        
    })
    .catch(error => console.error('Error:', error));
    
  };

  const obtenerColorBoton = (boton) => {
    // console.log('boton #:',boton);
    const ingrediente  = distribucionNombres[boton];
    if (ingrediente == '') return '#d3d3d3'; // Gris cuando no hay selección
    if (cambioIngrediente[boton] == true) return '#00FF28';
    if (cantidades[boton].cantidadActual < 30 && cantidades[boton].cantidadActual != -1) return '#ffd700'; // Amarillo cuando está vacío
     
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
        setNombreDistribStatus(data); // Guarda la respuesta 
    })
    .catch(error => console.error('Error:', error));


  },[distribucion]);
  

  useEffect(() => {
    fetchIngredientes();
    fetchDistribucion();
    fetchCantidades();
    fetchDistribucionNombres();
  }, [rellenarStatus,nombreDistribStatus,rellenarTodoStatus,borrarStatus,guardarStatus]);

  

  useEffect(()=>{
    console.log('cantidades',cantidades);
    console.log('posiciones',distribucionNombres);
  },[modalIsOpen]);

  //Notificaciones

  useEffect(() => {
    console.log('Estado de nombreDistribStatus:', nombreDistribStatus);
    
    if (nombreDistribStatus.code > 0){
      
      toast(
        
        <Notification 
            type={nombreDistribStatus.status} 
            errorMessage={nombreDistribStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [nombreDistribStatus]);

  useEffect(() => {
    console.log('Estado de rellenarStatus:', rellenarStatus);
    
    if (rellenarStatus.code > 0){
      
      toast(
        
        <Notification 
            type={rellenarStatus.status} 
            errorMessage={rellenarStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [rellenarStatus]);

  useEffect(() => {
    console.log('Estado de rellenarTodoStatus:', rellenarTodoStatus);
    
    if (rellenarTodoStatus.code > 0){
      
      toast(
        
        <Notification 
            type={rellenarTodoStatus.status} 
            errorMessage={rellenarTodoStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [rellenarTodoStatus]);

  useEffect(() => {
    console.log('Estado de borrarStatus:', borrarStatus);
    
    if (borrarStatus.code > 0){
      
      toast(
        
        <Notification 
            type={borrarStatus.status} 
            errorMessage={borrarStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [borrarStatus]);

  useEffect(() => {
    console.log('Estado de guardarStatus:', guardarStatus);
    
    if (guardarStatus.code > 0){
      
      toast(
        
        <Notification 
            type={guardarStatus.status} 
            errorMessage={guardarStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [guardarStatus]);
  useEffect(()=>{
    console.log('nombre',nombre)
  },[nombre]);
  

  return (
    <div>
      <div style={{width:"50%", top: 20, right: 20 }}>
        {console.log('distribucion front',distribucion)}
        <Select 
          options={nombres} 
          placeholder='Seleccione un set de posiciones'
          value = {distribucion}
          onChange={manejarCambioDistribucion}
          
        />
      </div>
      <div className={s.leyendaContainer}>
        <h3>Set de distribucion: {nombre}</h3>
      
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
          <span>Espacio Modificado/Sin Guardar</span>
          <div className={s.circuloLeyenda} style={{ backgroundColor: "#00ff28" }}></div>
        </div>
      </div>

      {/* Botonera */}
      <div className={s.botonera}>
        {/* Fila D y C */}
        <div className={s.filaVertical}>
          <div className={s.columnaVertical}>
            {Array.from({ length: 6 }, (_, i) => (
              <Button
                key={`D${6 - i}`}
                style={{ backgroundColor: obtenerColorBoton(27 - i) }}
                onClick={() => abrirModal(27 - i)}
                className={`${s.distribucionButton}`}
              >
                {`D${6 - i}`}
              </Button>
            ))}
          </div>
          <div className={s.separadorVertical} />
          <div className={s.columnaVertical}>
            {Array.from({ length: 6 }, (_, i) => (
              <Button
                key={`C${6 - i}`}
                style={{ backgroundColor: obtenerColorBoton(20 - i) }}
                onClick={() => abrirModal(20 - i)}
                className={`${s.distribucionButton}`}
              >
                {`C${6 - i}`}
              </Button>
            ))}
          </div>
        </div>

        {/* Fila B y A */}
        <div className={s.filaHorizontal}>
          {Array.from({ length: 6 }, (_, i) => (
            <Button
              key={`B${6 - i}`}
              style={{ backgroundColor: obtenerColorBoton(13 - i) }}
              onClick={() => abrirModal(13 - i)}
              className={`${s.distribucionButton}`}
            >
              {`B${6 - i}`}
            </Button>
          ))}
        </div>
        <div className={s.separadorHorizontal} />
        <div className={s.filaHorizontal}>
          {Array.from({ length: 6 }, (_, i) => (
            <Button
              key={`A${6 - i}`}
              style={{ backgroundColor: obtenerColorBoton(6 - i) }}
              onClick={() => abrirModal(6 - i)}
              className={`${s.distribucionButton}`}
            >
              {`A${6 - i}`}
            </Button>
          ))}
        </div>
      </div>

      <div style={{ display: "flex", justifyContent: "center", marginTop: "20px" }}>
        <Input
          type="text"
          value={nombreDisposicion}
          onChange={(e) => setNombreDisposicion(e.target.value)}
          placeholder={nombreDisposicion != ''?  nombreDisposicion : "Nombre de la disposición"}
        />
      </div>
      <div style={{ display: "flex", justifyContent: "center", marginTop: "20px" }}>
        <Button className={s.nBotonRecetas} onClick={guardarDisposicion}>Guardar Disposición</Button>
        
        {/*
        <Button className={s.nBotonRecetas} onClick={rellenarTodasBotellas}>Rellenar Todo</Button>
        <Button className={s.nBotonRecetas} onClick={borrarDisposicion}>Borrar Todo</Button>
       */}
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
          <div className='d-flex align-items-end'>
            <FormGroup>
              <Label for="cantidad">Contenido de la Botella</Label>
              <InputGroup>
                <Input
                  type="number"
                  id="cantidad"
                  value={cantidades[botonSeleccionado]?.cantidadActual || 0}
                  style={{ 
                    paddingRight: '0.5rem',
                  }}
                  disabled = {true}
                />
                <InputGroupText style={{
                  height: 'auto',
                  paddingLeft: '0.5rem',  // Espacio a la izquierda de "cm³"
                  paddingRight: '0.5rem',
                  borderLeft:"none",
                  borderTopLeftRadius: '0',
                  borderBottomLeftRadius: '0',
                  
                }}>
                  ml
                </InputGroupText>
                </InputGroup>
            </FormGroup>

            <FormGroup className='ml-2'>
              <Label for="cantidad">Cantidad Usada</Label>
              <InputGroup>
                <Input
                  type="number"
                  id="cantidad"
                  value={cantidades[botonSeleccionado]?.cantidadUsada || 0}
                  disabled={true}
                  style={{ 
                    paddingRight: '0.5rem',
                    //backgroundColor: "#58c48c",
                    color:'red'
                  }} // Ajusta el espacio dentro del input
                />
                <InputGroupText style={{
                  //backgroundColor: '#58c48c',
                  height: 'auto',
                  paddingLeft: '0.5rem',  // Espacio a la izquierda de "cm³"
                  paddingRight: '0.5rem',
                  borderLeft:"none",
                  borderTopLeftRadius: '0',
                  borderBottomLeftRadius: '0',
                  color:'red'
                  
                }}>
                  ml
                </InputGroupText>
              </InputGroup>
            </FormGroup>
            
          </div>

          <div style={{ display:"flex", justifyContent:"center", textAlign: 'center', margin: '30px 0' }}>
              <Button className={s.nBotonRecetas} onClick={rellenarCantidad}>Rellenar</Button>
          </div>
          <div style={{ display:"flex", justifyContent:"center", textAlign: 'center', margin: '10px 0' }}>
            <Button className={s.nBotonRecetas} onClick={guardarPosicion}>Ok</Button>
          </div>
        </ModalBody>
      </Modal>
    </div>
  );
};

export default Distribucion;
