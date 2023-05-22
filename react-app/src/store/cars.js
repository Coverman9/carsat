const ALL_CARS = "cars/ALL_CARS";
const ONE_CAR = "cars/ONE_CAR";
const CREATE_CAR = "cars/CREATE_CAR";
const UPDATE_CAR = "cars/UPDATE_CAR";
const DELETE_CAR = "cars/DELETE_CAR";

const allCarsAction = (cars) => ({
  type: ALL_CARS,
  cars,
});

const oneCarAction = (car) => ({
  type: ONE_CAR,
  car,
});

const createCarAction = (car) => ({
  type: CREATE_CAR,
  car,
});

const updateCarAction = (car) => ({
  type: UPDATE_CAR,
  car,
});

const deleteCarAction = (carId) => ({
  type: DELETE_CAR,
  carId,
});

///-------------------THUNK-------------------------

export const getAllCarsThunk = () => async (dispatch) => {
  const res = await fetch("/api/cars");
  const cars = await res.json();

  await dispatch(allCarsAction(cars));
};

export const getCarDetailThunk = (carId) => async (dispatch) => {
  const res = await fetch(`/api/cars/${carId}`);
  const car = await res.json();
  await dispatch(oneCarAction(car));
};

export const createCarThunk = (car) => async (dispatch) => {
  const { make, model, type, year, mileage, price, color, car_description } =
    car;
  const res = await fetch("/api/cars", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      make,
      model,
      type,
      year,
      mileage,
      price,
      color,
      car_description,
    }),
  });

  if (res.ok) {
    const newCar = await res.json();
    dispatch(createCarAction(newCar));
    return newCar;
  } else {
    const errors = await res.json();
    return errors;
  }
};

export const updateCarThunk = (car) => async (dispatch) => {
  const {
    make,
    model,
    type,
    year,
    mileage,
    price,
    color,
    car_description,
    carId,
  } = car;
  const res = await fetch(`/api/cars/${carId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      make,
      model,
      type,
      year,
      mileage,
      price,
      color,
      car_description,
    }),
  });

  if (res.ok) {
    const newCar = await res.json();
    dispatch(updateCarAction(newCar));
    return newCar;
  } else {
    const errors = await res.json();
    return errors;
  }
};

export const deleteCarThunk = (carId) => async (dispatch) => {
  const res = await fetch(`/api/cars/${carId}`, {
    method: "DELETE",
  });

  if (res.ok) {
    dispatch(deleteCarAction(carId));
  } else {
    const errors = await res.json();
    return errors;
  }
};
///------------------REDUCERS--------------------------

const initialState = {};

const cars = (state = initialState, action) => {
  let newState = {};
  switch (action.type) {
    case ALL_CARS:
      action.cars.cars?.forEach((car) => (newState[car.id] = car));
      return newState;
    case ONE_CAR:
      newState[action.car.car.id] = action.car.car;
      return newState;
    case CREATE_CAR:
      newState = { ...state };
      newState[action.car.id] = action.car;
      return newState;
    case UPDATE_CAR:
      console.log(state);
      return { ...state, [action.car.id]: action.car };
    case DELETE_CAR:
      newState = { ...state };
      delete newState[action.carId]
      return newState
    default:
      return state;
  }
};

export default cars;
