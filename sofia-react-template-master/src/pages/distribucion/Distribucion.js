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
      setIngredientes(list.data); // Guardar la lista en el estado
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

  useEffect(() => {
    fetchIngredientes();
    fetchDistribucion();
    fetchCantidades();
    const nombresFormateados = ingredientes.map((ingrediente) => ({
      value: ingrediente.nombre,
      label: ingrediente.nombre
    }));
    setIngredientesNombres(nombresFormateados);
    console.log(nombresFormateados)
  }, []);

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

  const guardarDisposicion = async () => {
    // Crear el array de disposición con las posiciones y cantidades
    const disposicionData = Object.entries(cantidades).map(([posicion, { cantidadActual, cantidadUsada, ingrediente }]) => ({
      posicion,
      cantidadActual,
      cantidadUsada,
      ingrediente: ingrediente?.value || null, // Verifica si el ingrediente está seleccionado
    }));

    // Estructura el payload con el nombre y la disposición
    const payload = {
      nombre: nombreDisposicion,
      disposicion: disposicionData,
    };

    console.log("Guardando disposición:", payload); // Verifica los datos en la consola

    // Enviar la solicitud POST al backend
    try {
      const response = await fetch('/guardar-disposicion', { // Reemplaza con la URL de tu endpoint
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (response.ok) {
        console.log('Disposición guardada exitosamente');
      } else {
        console.error('Error al guardar la disposición');
      }
    } catch (error) {
      console.error('Error en la solicitud:', error);
    }
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
    const ingrediente  = distribucionNombres[boton];
    if (!ingrediente) return '#d3d3d3'; // Gris cuando no hay selección
    if (ingrediente.value === '') return '#ffd700'; // Amarillo cuando está vacío
    return '#ff8b05'; // Naranja para los demás ingredientes
  };

  return (
    <div>
      <div style={{width:"50%", position: 'absolute', top: 20, right: 20 }}>
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
                style={{ backgroundColor: obtenerColorBoton(`D${7 - i}`) }}
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
                style={{ backgroundColor: obtenerColorBoton(`C${7 - i}`) }}
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
              style={{ backgroundColor: obtenerColorBoton(`B${7 - i}`) }}
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
              style={{ backgroundColor: obtenerColorBoton(`A${7 - i}`) }}
              onClick={() => abrirModal(`A${7 - i}`)}
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
              options={ingredientesNombres}
              value={ingredienteSeleccionado}
              onChange={manejarCambioIngrediente}
              placeholder="Seleccione un ingrediente"
            />
          </FormGroup>
          <FormGroup>
            <Label for="cantidad">Cantidad Usada</Label>
            <Input
              type="number"
              id="cantidad"
              value={cantidades[botonSeleccionado]?.cantidadUsada || 0}
              onChange={(e) => setCantidades((prev) => ({
                ...prev,
                [botonSeleccionado]: {
                  ...prev[botonSeleccionado],
                  cantidadUsada: parseFloat(e.target.value) || 0
                }
              }))}
            />

            <div style={{ display:"flex", justifyContent:"center", textAlign: 'center', margin: '30px 0' }}>
              <Button className={s.nBotonRecetas} onClick={rellenarCantidad}>Rellenar</Button>
            </div>
          </FormGroup>
          <div style={{ display:"flex", justifyContent:"center", textAlign: 'center', margin: '10px 0' }}>
            <Button className={s.nBotonRecetas} onClick={guardarPosicion}>Guardar Posición</Button>
          </div>
        </ModalBody>
      </Modal>
    </div>
  );
};

export default Distribucion;
