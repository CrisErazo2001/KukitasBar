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
      {/* Botones A1 a A7 */}
      <div className="d-flex justify-content-around mt-4 flex-wrap">
        {['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'].map((boton, index) => (
          <Button key={index} className={`${s.distribucionButton} m-2`} onClick={() => abrirModal(boton)}>
            {boton}
          </Button>
        ))}
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
