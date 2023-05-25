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
        <div>
          <h2>About Me</h2>
        </div>
        <div className="cards__container">
          <a href="https://github.com/Coverman9">
            <i class="fa-brands fa-github fa-flip fa-2xl"></i>
          </a>
        </div>
        <div className="cards__container">
          <a href="https://www.linkedin.com/in/emir-usubaliev-5904b0235/">
            <i class="fa-brands fa-linkedin fa-flip fa-2xl"></i>
          </a>
        </div>
        <div className="cards__container">
          <a href="https://www.instagram.com/usubalieve/">
            <i class="fa-brands fa-instagram fa-flip fa-2xl"></i>
          </a>
        </div>
      </div>
    </>
  );
};

export default LandingPage;
