const ALL_WISHLISTS_OF_CAR = "wishlists/ALL_WISHLISTS_OF_CAR";
const ALL_WISHLISTS_OF_USER = "wishlists/ALL_WISHLISTS_OF_USER";
const CREATE_WISHLIST = "wishlists/CREATE_WISHLIST";
const DELETE_WISHLIST = "wishlists/DELETE_WISHLIST";

const allCarWishlistsAction = (wishlists) => ({
  type: ALL_WISHLISTS_OF_CAR,
  wishlists,
});

const allUserWishlistsAction = (wishlists) => ({
  type: ALL_WISHLISTS_OF_USER,
  wishlists,
});

const createWishlistAction = (wishlist) => ({
  type: CREATE_WISHLIST,
  wishlist,
});

const deleteWishlistAction = (wishlistId) => ({
  type: DELETE_WISHLIST,
  wishlistId,
});

///-------------------THUNK-------------------------

export const getAllCarWishlistsThunk = (carId) => async (dispatch) => {

  const res = await fetch(`/api/wishlists/car/${carId}`);
  const wishlists = await res.json();

  await dispatch(allCarWishlistsAction(wishlists));
};

export const getAllUserWishlistsThunk = (userId) => async (dispatch) => {
  const res = await fetch(`/api/wishlists/user/${userId}`);
  const wishlists = await res.json();

  await dispatch(allUserWishlistsAction(wishlists));
};

export const createWishlistThunk = (wishlist) => async (dispatch) => {
  const { description, carId } = wishlist;
  const res = await fetch(`/api/wishlists/${carId}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      description,
    }),
  });

  if (res.ok) {
    const newWishlist = await res.json();
    dispatch(createWishlistAction(newWishlist));
    return newWishlist;
  } else {
    const errors = await res.json();
    return errors;
  }
};

export const deleteWishlistThunk = (wishlistId) => async (dispatch) => {
  const res = await fetch(`/api/wishlists/${wishlistId}`, {
    method: "DELETE",
  });

  if (res.ok) {
    dispatch(deleteWishlistAction(wishlistId));
  } else {
    const errors = await res.json();
    return errors;
  }
};
///------------------REDUCERS--------------------------

const initialState = {};

const wishlists = (state = initialState, action) => {
  let newState = {};
  switch (action.type) {
    case ALL_WISHLISTS_OF_CAR:
      action.wishlists.wishlists.forEach((wishlist) => (newState[wishlist.id] = wishlist));
      return newState;
    case ALL_WISHLISTS_OF_USER:
      action.wishlists.wishlists.forEach((wishlist) => (newState[wishlist.id] = wishlist));
      return newState;
    case CREATE_WISHLIST:
      newState = { ...state };
      newState[action.wishlist.id] = action.wishlist;
      return newState;
    case DELETE_WISHLIST:
      newState = { ...state };
      delete newState[action.wishlistId];
      return newState;
    default:
      return state;
  }
};

export default wishlists;
