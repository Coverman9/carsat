import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteWishlistThunk } from "../../store/wishlists";

const RemoveWishModal = ({wishlist}) => {
  const { closeModal } = useModal();
  const dispatch = useDispatch();

  const confirmDelete = async () => {
    await dispatch(deleteWishlistThunk(wishlist.id));
    closeModal();
  };

  return (
    <>
      <h2>Remove Car</h2>
      <p>Are you sure you want to remove car from your wishlist?</p>
      <button onClick={confirmDelete}>Yes</button>
      <button onClick={closeModal}>No</button>
    </>
  );
};

export default RemoveWishModal;
