import React, { useState } from 'react';
import { Modal, ModalHeader, ModalBody, Button, Row, Col, Input, FormGroup, Label } from 'reactstrap';
import Select from 'react-select';
import s from './Distribucion.module.scss';

const Distribucion = () => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [botonSeleccionado, setBotonSeleccionado] = useState('');
  const [ingredienteSeleccionado, setIngredienteSeleccionado] = useState(null);

  const [cantidades, setCantidades] = useState(
    Array.from({ length: 28 }, (_, i) => ({
      cantidadActual: 750,
      cantidadUsada: 0,
      ingrediente: null
    })).reduce((acc, _, i) => {
      const fila = String.fromCharCode(65 + Math.floor(i / 7)); // Filas A, B, C, D
      const col = (i % 7) + 1; // Columnas 1 a 7
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

  return (
    <div>
      {/* Botonera */}
      <div className={s.botonera}>


        
        {/* Imagen de fondo entre las columnas C y D */}
        <div className={s.imagenSeparador}>
          <img src='../../assets/Frame_21.png' alt="Fondo" className={s.imagenCentral} />
        </div>

        {/* Separador vertical con la imagen */}
        <div className={s.filaVertical}>
          <div className={s.columnaVertical}>
            {Array.from({ length: 7 }, (_, i) => (
              <Button
                key={`C${7 - i}`} // C7 a C1
                className={`${s.distribucionButton} m-2`}
                onClick={() => abrirModal(`C${7 - i}`)}
              >
                {`C${7 - i}`}
              </Button>
            ))}
          </div>

          {/* Separador entre Fila A y Fila B */}
          <div className={s.separadorVertical} />
          <div className={s.columnaVertical}>
            {Array.from({ length: 7 }, (_, i) => (
              <Button
                key={`D${7 - i}`} // D7 a D1
                className={`${s.distribucionButton} m-2`}
                onClick={() => abrirModal(`D${7 - i}`)}
              >
                {`D${7 - i}`}
              </Button>
            ))}
          </div>
        </div>

        {/* Fila A */}
        <div className={s.filaHorizontal}>
          {Array.from({ length: 7 }, (_, i) => (
            <Button
              key={`A${7 - i}`} // A7 a A1
              className={`${s.distribucionButton} m-2`}
              onClick={() => abrirModal(`A${7 - i}`)}
            >
              {`A${7 - i}`}
            </Button>
          ))}
        </div>

        {/* Separador entre Fila A y Fila B */}
        <div className={s.separadorHorizontal} />

        {/* Fila B */}
        <div className={s.filaHorizontal}>
          {Array.from({ length: 7 }, (_, i) => (
            <Button
              key={`B${7 - i}`} // B7 a B1
              className={`${s.distribucionButton} m-2`}
              onClick={() => abrirModal(`B${7 - i}`)}
            >
              {`B${7 - i}`}
            </Button>
          ))}
        </div>

      </div>

      {/* Modal */}
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