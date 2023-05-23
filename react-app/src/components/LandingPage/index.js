import LoginFormModal from "../LoginFormModal";
import OpenModalButton from "../OpenModalButton";
import "./LandingPage.css";

const LandingPage = () => {
  return (
    <>
      <div className="hero-container">
        <h1>GET NEW CAR!</h1>
        <p>What are you waiting for?</p>
        <div className="hero-btns">
          <button>
            <OpenModalButton
              buttonText="GET STARTED"
              modalComponent={<LoginFormModal />}
            />
          </button>
        </div>
      </div>
      <div className="cards">
        <h2>About Me</h2>
        <div className="cards__container">
          <div className="cards__wrapper"></div>
        </div>
      </div>
    </>
  );
};

export default LandingPage;
