import React, { useState } from 'react';
import { Modal, ModalHeader, ModalBody, Button, Row, Col, Input, FormGroup, Label } from 'reactstrap';
import Select from 'react-select';
import s from './Distribucion.module.scss';

const Distribucion = () => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [botonSeleccionado, setBotonSeleccionado] = useState('');
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);
  const [nombreDisposicion, setNombreDisposicion] = useState('');
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

  const ingredientesPorDefecto = [
    { value: 'Vacío', label: 'Vacío' },
    { value: 'Ron', label: 'Ron' },
    { value: 'Tequila', label: 'Tequila' },
    { value: 'Vodka', label: 'Vodka' },
    { value: 'Triple Sec', label: 'Triple Sec' }
  ];

  const abrirModal = (boton) => {
    setBotonSeleccionado(boton);
    setIngredienteSeleccionado(cantidades[boton].ingrediente);
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
    const { ingrediente } = cantidades[boton];
    if (!ingrediente) return '#d3d3d3'; // Gris cuando no hay selección
    if (ingrediente.value === 'Vacío') return '#ffd700'; // Amarillo cuando está vacío
    return '#ff8b05'; // Naranja para los demás ingredientes
  };

  return (
    <div>
      {/* Selector en la parte superior derecha */}
      <div style={{width:"50%", position: 'absolute', top: 20, right: 20 }}>
        <Select options={ingredientesPorDefecto} placeholder="Seleccionar opción" />
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
              options={ingredientesPorDefecto}
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

          <Button color="success" className={s.modalButton} onClick={rellenarCantidad}>
            Rellenar
          </Button>
          <Button color="primary" className={s.modalButton} onClick={guardarPosicion}>
            Guardar
          </Button>
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


{/* 
import React, { useState } from 'react';
import { Modal, ModalHeader, ModalBody, Button, Row, Col, Input, FormGroup, Label } from 'reactstrap';
import Select from 'react-select'; // Asegúrate de tener esta librería instalada
import s from './Distribucion.module.scss'; // Importa los estilos del modal

const Distribucion = () => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [botonSeleccionado, setBotonSeleccionado] = useState('');
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);
  
  // Estado para cantidades actuales y usadas para cada botón
  const [cantidades, setCantidades] = useState({
    A1: { cantidadActual: 750, cantidadUsada: 0, ingrediente: null },
    A2: { cantidadActual: 750, cantidadUsada: 0, ingrediente: null },
    A3: { cantidadActual: 750, cantidadUsada: 0, ingrediente: null },
    A4: { cantidadActual: 750, cantidadUsada: 0, ingrediente: null },
    A5: { cantidadActual: 750, cantidadUsada: 0, ingrediente: null },
    A6: { cantidadActual: 750, cantidadUsada: 0, ingrediente: null },
    A7: { cantidadActual: 750, cantidadUsada: 0, ingrediente: null },
  });

// Opciones para el selector
const ingredientesPorDefecto = [
  { value: 'Vacío', label: 'Vacío' },
  { value: 'Ron', label: 'Ron' },
  { value: 'Tequila', label: 'Tequila' },
  { value: 'Vodka', label: 'Vodka' },
  { value: 'Triple Sec', label: 'Triple Sec' }
  ];

  // Maneja la apertura del modal
  const abrirModal = (boton) => {
    setBotonSeleccionado(boton);
    setIngredienteSeleccionado(cantidades[boton].ingrediente); // Carga el ingrediente guardado
    setModalIsOpen(true);
  };

  const cerrarModal = () => {
    setModalIsOpen(false);
  };

  // Actualiza el ingrediente seleccionado
  const manejarCambioIngrediente = (ingrediente) => {
    setIngredienteSeleccionado(ingrediente);
  };

  // Función para rellenar la cantidad usada con la cantidad actual
  const rellenarCantidad = () => {
    setCantidades((prev) => ({
      ...prev,
      [botonSeleccionado]: {
        ...prev[botonSeleccionado],
        cantidadUsada: prev[botonSeleccionado].cantidadActual
      }
    }));
  };

  // Función para guardar la posición
  const guardarPosicion = () => {
    setCantidades((prev) => ({
      ...prev,
      [botonSeleccionado]: {
        ...prev[botonSeleccionado],
        ingrediente: ingredienteSeleccionado, // Guarda el ingrediente seleccionado
      }
    }));
    cerrarModal();
  };

  return (
    <div>
   
      <div className={s.botonera}>
        {['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'].map((boton, index) => (
          <Button key={index} className={`${s.distribucionButton} m-2`} onClick={() => abrirModal(boton)}>
            {boton}
          </Button>
        ))}
      </div>

      <Modal isOpen={modalIsOpen} toggle={cerrarModal} centered className={s.modalCustom}>
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
              options={ingredientesPorDefecto}
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
                  onChange={(e) => 
                    setCantidades((prev) => ({
                      ...prev,
                      [botonSeleccionado]: {
                        ...prev[botonSeleccionado],
                        cantidadActual: Number(e.target.value)
                      }
                    }))
                  }
                  className={s.modalInput}
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
                  onChange={(e) => 
                    setCantidades((prev) => ({
                      ...prev,
                      [botonSeleccionado]: {
                        ...prev[botonSeleccionado],
                        cantidadUsada: Number(e.target.value)
                      }
                    }))
                  }
                  className={s.modalInput}
                />
              </FormGroup>
            </Col>
          </Row>

          <div className="d-flex justify-content-center mt-4">
            <Button className={`${s.modalButton}`} onClick={rellenarCantidad}>
              Rellenar
            </Button>
            <Button className={`${s.modalButton} ${s.modalButtonSecondary}`} onClick={guardarPosicion}>
              Guardar Posición
            </Button>
          </div>
        </ModalBody>
      </Modal>
    </div>
  );
};

export default Distribucion;
*/}