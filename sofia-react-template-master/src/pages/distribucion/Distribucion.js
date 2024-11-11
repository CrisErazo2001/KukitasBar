import React, { useState, useEffect } from 'react';
import { Modal, ModalHeader, ModalBody, Button, Row, Col, Input, FormGroup, Label, InputGroup, InputGroupText, Tooltip  } from 'reactstrap';
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
  const [mostrarInputNombre, setMostrarInputNombre] = useState(false);  // Nuevo estado para visibilidad del campo de entrada
  const [ingredientes, setIngredientes] = useState(['']);
  const [distribucionNombres, setDistribucionNombres] = useState([]);
  const [cantidades, setCantidades] = useState(Array.from({ length: 24 }, () => ({ cantidadActual: -1, cantidadUsada: 0 })));
  const [cambioIngrediente, setCambioIngrediente] = useState(Array.from({ length: 24 }, () => (false)));
  const [nombres, setNombres] = useState([]);
  const [distribucion, setDistribucion] = useState('');
  const [nombreDistribStatus, setNombreDistribStatus] = useState({}); //seleccion de una distrib
  const [rellenarStatus,setRellenarStatus] = useState({});
  const [rellenarTodoStatus,setRellenarTodoStatus] = useState({});
  const [borrarStatus,setBorrarStatus] = useState({});
  const [guardarStatus,setGuardarStatus] = useState({});
  const [nombre,setNombre] = useState('');
  //



  /* Tooltip */
  const [tooltips, setTooltips] = useState(Array.from({ length: 24 }, () => false));

  const toggleTooltip = (index) => {
    setTooltips((prevTooltips) => {
        const newTooltips = [...prevTooltips];
        newTooltips[index] = !newTooltips[index];
        return newTooltips;
    });
};

/* Tabla Nueva */
const [tablaVisible, setTablaVisible] = useState(false);
const toggleTabla = () => {
  setTablaVisible(!tablaVisible);
};

// Agregar este componente dentro de Distribucion o en un archivo separado
// Agregar este componente dentro de Distribucion o en un archivo separado
const TablaInformacion = ({ distribucionNombres, cantidades }) => {


  return (
    <div className={s.tablaInformacionContainer}>
      <h4>Información distribución</h4>
      <table className={s.tablaInformacion}>
        <thead>
          <tr>
            <th style={{fontWeight: 'bold'}}>Posición</th>
            <th style={{fontWeight: 'bold'}}>Ingrediente</th>
            <th style={{fontWeight: 'bold'}}>Contenido en Botella (ml)</th>
            <th style={{fontWeight: 'bold'}}>Disponible (ml)</th>
          </tr>
        </thead>
        <tbody>
          {Array.from({ length: 24 }, (_, i) => {
            // Calcular el valor de Disponible (ml)
            const disponible = cantidades[i]?.cantidadActual - cantidades[i]?.cantidadUsada || '-';

            // Determinar si el valor es menor o igual a 50 ml
            const claseDisponible = disponible <= 50 ? s.textoRojo : '';

            // Condicional para mostrar "-" si el ingrediente es N/A
            const contenidoBotella = distribucionNombres[i] === 'N/A' ? '-' : cantidades[i]?.cantidadActual || '-';
            const disponibleTexto = distribucionNombres[i] === 'N/A' ? '-' : disponible;

            return (
              <tr key={i}>
                <td style={{fontWeight: 'bold'}}>
                  {i < 6 ? 'D' : i < 12 ? 'C' : i < 18 ? 'B' : 'A'}
                  {6 - (i % 6)}
                </td>
                <td>{distribucionNombres[i] || 'N/A'}</td>
                <td>{contenidoBotella}</td>
                <td className={claseDisponible}>{disponibleTexto}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};



/* Fin Tabla Nueva */


  /* Fin Tooltip */
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
    // cantidades[boton] = distribucionNombres[boton].cant;
    setModalIsOpen(true);
  };


  const cerrarModal = () => {
    setModalIsOpen(false);
  };


  /* ANTIGUO 
  const manejarCambioIngrediente = (ingrediente) => {
    console.log('ingrediente', ingrediente)
    setIngredienteSeleccionado(ingrediente);
  };
  /* ANTIGUO */

  /* NUEVO */
  const manejarCambioIngrediente = (ingrediente) => {
    console.log('ingrediente seleccionado:', ingrediente);
    setIngredienteSeleccionado(ingrediente);

    // Actualizar el contenido de la botella para el botón seleccionado
    const nuevaCantidad = obtenerCantidadPorIngrediente(ingrediente); // Función para obtener cantidad del ingrediente

    setCantidades((prevCantidades) => {
        const nuevasCantidades = [...prevCantidades];
        nuevasCantidades[botonSeleccionado] = {
            ...nuevasCantidades[botonSeleccionado],
            cantidadActual: nuevaCantidad,
        };
        return nuevasCantidades;
    });
};
const obtenerCantidadPorIngrediente = (ingrediente) => {
  // Aquí se determina la cantidad asociada al ingrediente. 
  // Por ejemplo, una búsqueda en un array u objeto con las cantidades de ingredientes.
  return ingrediente.cantidadActual || "-";
};


  /* NUEVO */

  const manejarCambioDistribucion = (dis) => {
    let algunValorEsTrue = false;

    for (let i = 0; i < cambioIngrediente.length; i++) {
      if (cambioIngrediente[i] === true) {
        algunValorEsTrue = true;
        break; // Detenemos el bucle porque encontramos un valor `true`
      }
    }

    if (algunValorEsTrue){
      toast(
        
        <Notification 
            type='warning'
            errorMessage='Has realizado cambios sin guardarlos'
            withIcon 
        />, 
        options
      );

    }
    else{
      console.log('distribucion',dis);
      setDistribucion(dis); 
    }
      
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

  {/* Anterior GuardarPosicion */}
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
  {/* Anterior GuardarPosicion */}

  /* Nuevo */
  const toggleMostrarInputNombre = () => setMostrarInputNombre(!mostrarInputNombre);

  /* */
  const guardarDisposicion = () => {

    fetch('/posicion/save-distribucion', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        nombreSeleccionado: distribucion,
        nuevoNombre: nombreDisposicion, 
        posiciones: distribucionNombres
      })
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setGuardarStatus(data); // Guarda la respuesta 
        setMostrarInputNombre(false);  // Ocultar el campo de entrada al guardar
        
    })
    .catch(error => console.error('Error:', error));

    setCambioIngrediente(Array.from({ length: 24 }, () => (false)));
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
    if (cambioIngrediente[boton] == true) return '#00FF28';
    if (ingrediente == '') return '#d3d3d3'; // Gris cuando no hay selección
    if (cantidades[boton].cantidadActual < 30 && cantidades[boton].cantidadActual != -1) return '#ffd700'; // Amarillo cuando está vacío
     
    return '#ff8b05'; // Naranja para los demás ingredientes
  };

 
  useEffect(()=>{
    
    fetch('/posicion/set', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({nombre: distribucion,posiciones: distribucionNombres})
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
      <div className='mb-3' style={{
        width:'100%',
        display:'flex',
        justifyContent:'center'
      }}>
        <div style={{width:"50%", top: 20, right: 20 }}>
          {console.log('distribucion front',distribucion)}
          <Select 
            options={nombres} 
            placeholder='Seleccione un set de posiciones'
            value = {distribucion}
            onChange={manejarCambioDistribucion}
          />
        </div>
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

      <div>
        {/* Botón para mostrar/ocultar la tabla */}
        <button className={`${s.nBotonRecetas} mt-3 mb-3`}
          onClick={toggleTabla} 
          style={{ backgroundColor: tablaVisible ? 'red' : '#ff8b05', color: 'white', fontWeight: 'bold' }}
        >
          {tablaVisible ? 'Esconder Tabla' : 'Ver Tabla de Cantidades'}
        </button>

        {/* Tabla de Información */}
        {tablaVisible && (
          <TablaInformacion distribucionNombres={distribucionNombres} cantidades={cantidades} />
        )}
      </div>

      <div className={s.botonera}>

        {/* Fila D */}
        <div className={s.filaVertical}>
          <div className={s.columnaVertical}>
            {Array.from({ length: 6 }, (_, i) => (
            <div style={{display:'flex'}}>
              <Button
                key={`D${6 - i}`}
                id={`tooltip-${23 - i}`} //
                style={{ backgroundColor: obtenerColorBoton(23 - i) }}
                onClick={() => abrirModal(23 - i)}
                className={`${s.distribucionButton}`}
              >
                {`D${6 - i}`}
              </Button>
              <Tooltip
                isOpen={tooltips[23 - i]}
                target={`tooltip-${23 - i}`}
                toggle={() => toggleTooltip(23 - i)}
              >
                {/* Aquí, usando JSX para mostrar saltos de línea con <br /> */}
                <div>
                  <strong>Ingrediente: </strong>{distribucionNombres[23 - i] || 'N/A'}
                  <br />
                  <strong>Contenido Botella: </strong>{cantidades[23 - i]?.cantidadActual || 0} ml
                  <br />
                  <strong>Disponible: </strong>
                  { 
                    // Realizamos el cálculo de la cantidad disponible
                    cantidades[23 - i]?.cantidadActual && cantidades[23 - i]?.cantidadUsada 
                      ? (cantidades[23 - i].cantidadActual - cantidades[23 - i].cantidadUsada) + " ml"
                      : "-"
                  }
                </div>
              </Tooltip>
            </div>
              
            ))}
          </div>
          <div className={s.separadorVertical} />

          {/* Fila C */}
          <div className={s.columnaVertical}>
            {Array.from({ length: 6 }, (_, i) => (
              <div>
              <Button
                key={`C${6 - i}`}
                id={`tooltip-${17 - i}`}
                style={{ backgroundColor: obtenerColorBoton(17 - i) }}
                onClick={() => abrirModal(17 - i)}
                className={`${s.distribucionButton}`}
              >
                {`C${6 - i}`}
              </Button>
              <Tooltip
                isOpen={tooltips[17 - i]}
                target={`tooltip-${17 - i}`}
                toggle={() => toggleTooltip(17 - i)}
              >
                {/* Aquí, usando JSX para mostrar saltos de línea con <br /> */}
                <div>
                  <strong>Ingrediente: </strong>{distribucionNombres[17 - i] || 'N/A'}
                  <br />
                  <strong>Contenido Botella: </strong>{cantidades[17 - i]?.cantidadActual || "-"} ml
                  <br />
                  <strong>Disponible: </strong>
                  { 
                    // Realizamos el cálculo de la cantidad disponible
                    cantidades[17 - i]?.cantidadActual && cantidades[17 - i]?.cantidadUsada 
                      ? (cantidades[17 - i].cantidadActual - cantidades[17 - i].cantidadUsada) + " ml"
                      : "-"
                  }
                </div>
              </Tooltip>
              
              </div>
            ))}
          </div>
        </div>
        

        {/* Fila B y A */}
        <div className={s.filaHorizontal}>
          {Array.from({ length: 6 }, (_, i) => (
            <div>
              <Button
                key={`B${6 - i}`}
                id={`tooltip-${11 - i}`}
                style={{ backgroundColor: obtenerColorBoton(11 - i) }}
                onClick={() => abrirModal(11 - i)}
                className={`${s.distribucionButton}`}
              >
                {`B${6 - i}`}
              </Button>
              <Tooltip
                isOpen={tooltips[11 - i]}
                target={`tooltip-${11 - i}`}
                toggle={() => toggleTooltip(11 - i)}
              >
                {/* Aquí, usando JSX para mostrar saltos de línea con <br /> */}
                <div>
                  <strong>Ingrediente: </strong>{distribucionNombres[11 - i] || 'N/A'}
                  <br />
                  <strong>Contenido Botella: </strong>{cantidades[11 - i]?.cantidadActual || 0} ml
                  <br />
                  <strong>Disponible: </strong>
                  { 
                    // Realizamos el cálculo de la cantidad disponible
                    cantidades[11 - i]?.cantidadActual && cantidades[11 - i]?.cantidadUsada 
                      ? (cantidades[11 - i].cantidadActual - cantidades[11 - i].cantidadUsada) + " ml"
                      : "-"
                  }
                </div>
              </Tooltip>
            </div>
          ))}
        </div>
        <div className={s.separadorHorizontal} />
        <div className={s.filaHorizontal}>
          {Array.from({ length: 6 }, (_, i) => (
            <div>
              <Button
                key={`A${6 - i}`}
                id={`tooltip-${5 - i}`}
                style={{ backgroundColor: obtenerColorBoton(5 - i) }}
                onClick={() => abrirModal(5 - i)}
                className={`${s.distribucionButton}`}
              >
                {`A${6 - i}`}
              </Button>
              <Tooltip
                isOpen={tooltips[5 - i]}
                target={`tooltip-${5 - i}`}
                toggle={() => toggleTooltip(5 - i)}
              >
                {/* Aquí, usando JSX para mostrar saltos de línea con <br /> */}
                <div>
                  <strong>Ingrediente: </strong>{distribucionNombres[5 - i] || 'N/A'}
                  <br />
                  <strong>Contenido Botella: </strong>{cantidades[5 - i]?.cantidadActual || 0} ml
                  <br />
                  <strong>Disponible: </strong>
                  { 
                    // Realizamos el cálculo de la cantidad disponible
                    cantidades[5 - i]?.cantidadActual && cantidades[5 - i]?.cantidadUsada 
                      ? (cantidades[5 - i].cantidadActual - cantidades[5 - i].cantidadUsada) + " ml"
                      : "-"
                  }
                </div>
              </Tooltip>
            </div>
          ))}
        </div>

      </div>
      {/* Botones para Guardar */}
      <div style={{ display: "flex", justifyContent: "center", marginTop: "20px" }}>
        {/* Botón de Guardar Como */}
        <Button className={s.nBotonRecetas} onClick={toggleMostrarInputNombre}>
          Guardar Como
        </Button>
      </div>

      {/* Campo de entrada para el nombre de disposición (oculto/invisible por defecto) */}
      {mostrarInputNombre && (
        <div style={{ display: "flex", justifyContent: "center", marginTop: "20px" }}>
          <Input
            type="text"
            style={{maxWidth:'400px'}}
            value={nombreDisposicion}
            onChange={(e) => setNombreDisposicion(e.target.value)}
            placeholder={nombreDisposicion !== '' ? nombreDisposicion : "Nuevo nombre de la disposición"}
          />
          <div className='mb-5'></div>
          <div className='mb-5'></div>
          <div className='mb-5'></div>
        </div>
      )}

 
      <div style={{ display: "flex", justifyContent: "center", marginTop: "20px" }}>
        <Button className={s.nBotonRecetas} onClick={guardarDisposicion}>Guardar Disposición</Button>
        
        {/*
        <Button className={s.nBotonRecetas} onClick={rellenarTodasBotellas}>Rellenar Todo</Button>
        <Button className={s.nBotonRecetas} onClick={borrarDisposicion}>Borrar Todo</Button>
       */}
        </div>
      <Modal 
        isOpen={modalIsOpen} 
        toggle={cerrarModal} 
        onClick={(e) => {
          // Detecta si el clic fue fuera del modal
          if (e.target.classList.contains("modal")) {
            cerrarModal();  // Cierra el modal si se hace clic fuera de él
          }
        }} 
      >
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
                  value={cantidades[botonSeleccionado]?.cantidadActual || '-'}
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
              <Label for="cantidad">Cantidad Disponible</Label>
              <InputGroup>
                <Input
                  type="number"
                  id="cantidad"
                  value={cantidades[botonSeleccionado]?.cantidadActual - cantidades[botonSeleccionado]?.cantidadUsada || '-'}
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
