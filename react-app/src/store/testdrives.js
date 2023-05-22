const ALL_TESTDRIVES_OF_CAR = "testdrives/ALL_TESTDRIVES_OF_CAR";
const ALL_TESTDRIVES_OF_USER = "testdrives/ALL_TESTDRIVES_OF_USER";
const CREATE_TESTDRIVE = "testdrives/CREATE_TESTDRIVE";
const UPDATE_TESTDRIVE = "testdrives/UPDATE_TESTDRIVE";
const CANCEL_TESTDRIVE = "testdrives/CANCEL_TESTDRIVE";

const allCarTestdrivesAction = (testdrives) => ({
  type: ALL_TESTDRIVES_OF_CAR,
  testdrives,
});

const allUserTestdrivesAction = (testdrives) => ({
  type: ALL_TESTDRIVES_OF_USER,
  testdrives,
});

const createTestdriveAction = (testdrive) => ({
  type: CREATE_TESTDRIVE,
  testdrive,
});

const updateTestdriveAction = (testdrive) => ({
  type: UPDATE_TESTDRIVE,
  testdrive,
});

const cancelTestDriveAction = (testdriveId) => ({
  type: CANCEL_TESTDRIVE,
  testdriveId,
});

///-------------------THUNK-------------------------

export const getAllCarTestdrivesThunk = (carId) => async (dispatch) => {
  const res = await fetch(`/api/testdrives/car/${carId}`);
  const testdrives = await res.json();

  await dispatch(allCarTestdrivesAction(testdrives));
};

export const getAllUserTestdrivesThunk = (userId) => async (dispatch) => {
  const res = await fetch(`/api/testdrives/user/${userId}`);
  const testdrives = await res.json();

  await dispatch(allUserTestdrivesAction(testdrives));
};

export const createTestdriveThunk = (testdrive) => async (dispatch) => {
  const { testdrive_date, carId } = testdrive;
  const res = await fetch(`/api/testdrives/${carId}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      testdrive_date,
    }),
  });

  if (res.ok) {
    const newTestdrive = await res.json();
    dispatch(createTestdriveAction(newTestdrive));
    return newTestdrive;
  } else {
    const errors = await res.json();
    return errors;
  }
};

export const updateTestdriveThunk = (testdrive) => async (dispatch) => {
  const { testdrive_date, testdriveId } = testdrive;
  const res = await fetch(`/api/testdrives/${testdriveId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      testdrive_date,
    }),
  });

  if (res.ok) {
    const newTestdrive = await res.json();
    dispatch(updateTestdriveAction(newTestdrive));
    return newTestdrive;
  } else {
    const errors = await res.json();
    return errors;
  }
};

export const cancelTestdriveThunk = (testdriveId) => async (dispatch) => {
  const res = await fetch(`/api/testdrives/${testdriveId}`, {
    method: "DELETE",
  });

  if (res.ok) {
    dispatch(cancelTestDriveAction(testdriveId));
  } else {
    const errors = await res.json();
    return errors;
  }
};
///------------------REDUCERS--------------------------

const initialState = {};

const testdrives = (state = initialState, action) => {
  let newState = {};
  switch (action.type) {
    case ALL_TESTDRIVES_OF_CAR:
      action.testdrives.testdrives.forEach(
        (testdrive) => (newState[testdrive.id] = testdrive)
      );
      return newState;
    case ALL_TESTDRIVES_OF_USER:
      action.testdrives.testdrives.forEach(
        (testdrive) => (newState[testdrive.id] = testdrive)
      );
      return newState;
    case CREATE_TESTDRIVE:
      newState = { ...state };
      newState[action.testdrive.id] = action.testdrive;
      return newState;
    case UPDATE_TESTDRIVE:
      return { ...state, [action.testdrive.id]: action.testdrive };
    case CANCEL_TESTDRIVE:
      newState = { ...state };
      delete newState[action.testdriveId];
      return newState;
    default:
      return state;
  }
};

export default testdrives;
