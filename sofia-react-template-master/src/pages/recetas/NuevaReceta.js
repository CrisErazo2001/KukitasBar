import React, { useState } from 'react';
import { Button, FormGroup, Label, Input } from 'reactstrap';
import Select from 'react-select'; // Select con buscador integrado
import s from "../ingredientes/Ingredientes.module.scss";

const NuevaReceta = ({ onClose, setRecetas, recetas, receta, modoEditar, ingredientes }) => {
  const ingredientesPorDefecto = ingredientes.length > 0 ? ingredientes : [
    { nombre: 'Ron', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Vodka', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Tequila', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Whiskey', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Triple Sec', tipo: 'Alcohol', costo: '1.23', cantidad: '750' }
  ];

  const [nombreReceta, setNombreReceta] = useState(receta ? receta.nombre : '');
  const [ingredientesSeleccionados, setIngredientesSeleccionados] = useState(
    receta ? receta.ingredientes.map(ing => ({ label: ing.nombre, value: ing })) : []
  );

  const opcionesIngredientes = [
    { label: "Vacío", value: null },
    ...ingredientesPorDefecto.map(ing => ({ label: ing.nombre, value: ing }))
  ];

  const manejarCambioIngrediente = (index, ingrediente) => {
    const nuevosIngredientes = [...ingredientesSeleccionados];
    nuevosIngredientes[index] = ingrediente;
    setIngredientesSeleccionados(nuevosIngredientes);
  };

  const guardarReceta = () => {
    const nuevaReceta = {
      nombre: nombreReceta,
      ingredientes: ingredientesSeleccionados.filter(ing => ing.value !== null).map(ing => ing.value)
    };

    if (modoEditar) {
      const recetasActualizadas = recetas.map(rec =>
        rec.nombre === receta.nombre ? nuevaReceta : rec
      );
      setRecetas(recetasActualizadas);
    } else {
      setRecetas([...recetas, nuevaReceta]);
    }

    onClose();
  };

  return (
    <div className={s.total}>
      <div className={s.cuadroGeneral}>
        <h2>{modoEditar ? 'Editar Receta' : 'Crear Nueva Receta'}</h2>
        
        <FormGroup>
          <Label for="nombreReceta">Nombre de la Receta</Label>
          <Input
            type="text"
            id="nombreReceta"
            value={nombreReceta}
            onChange={(e) => setNombreReceta(e.target.value)}
            placeholder="Introduce el nombre de la receta"
          />
        </FormGroup>

        {/* Contenedor en una sola columna */}
        <div className={s.recetaContainer}>
          {[...Array(10)].map((_, index) => (
            <div key={index} className={s.recetaFila}>
              <Label className={s.nlabel}>Ingrediente {index + 1}</Label>
              <Select
                className={s.ingredienteRecetaSelector}
                value={ingredientesSeleccionados[index] || { nlabel: "Vacío", value: null }}
                onChange={(ingrediente) => manejarCambioIngrediente(index, ingrediente)}
                options={opcionesIngredientes}
                isSearchable={true}
                placeholder={`Selecciona ingrediente ${index + 1}`}
              />
            </div>
          ))}
        </div>

        <div className="d-flex justify-content-center mt-4">
          <Button className={`${s.nBotonRecetas} mr-3`} onClick={guardarReceta}>Guardar Receta</Button>
          <Button className={s.nBotonRecetas} onClick={onClose}>Cancelar</Button>
        </div>
        <div className='mb-5'></div>
        <hr></hr>
        <div className='mb-4'></div>
      </div>
    </div>
  );
};

export default NuevaReceta;
