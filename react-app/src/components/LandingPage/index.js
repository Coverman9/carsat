import video from "./video-1.mp4";
import "./LandingPage.css";
const LandingPage = () => {
  return (
    <>
      <div className="hero-container">
        <video src={video} autoPlay loop muted />
        <h1>GET NEW CAR!</h1>
        <p>What are you waiting for?</p>
        <div className="hero-btns">
          <button>GET STARTED</button>
        </div>
      </div>
      <div className="cards">
        <h2>Check out these EPIC Unaas</h2>
        <div className="cards__container">
          <div className="cards__wrapper">
            <ul className="cards__items">
              <li className="cards__item">
                <figure
                  className="cards__item__pic-wrap"
                  data-category="Mercedes"
                >
                  <img
                    className="cards__item__img"
                    alt="img"
                    src="https://carloson.ru/uploads/images/cars/62/5517804b683b93f62d6c03612223a1bd-740x507.jpg"
                  />
                </figure>
                <div className="cards__item__info">
                  <h5 className="cards__item__text">Hello</h5>
                </div>
              </li>
              <li className="cards__item">
                <figure
                  className="cards__item__pic-wrap"
                  data-category="Mercedes"
                >
                  <img
                    className="cards__item__img"
                    alt="img"
                    src="https://carloson.ru/uploads/images/cars/62/5517804b683b93f62d6c03612223a1bd-740x507.jpg"
                  />
                </figure>
                <div className="cards__item__info">
                  <h5 className="cards__item__text">Hello</h5>
                </div>
              </li>
            </ul>
            <ul className="cards__items">
              <li className="cards__item">
                <figure
                  className="cards__item__pic-wrap"
                  data-category="Mercedes"
                >
                  <img
                    className="cards__item__img"
                    alt="img"
                    src="https://carloson.ru/uploads/images/cars/62/5517804b683b93f62d6c03612223a1bd-740x507.jpg"
                  />
                </figure>
                <div className="cards__item__info">
                  <h5 className="cards__item__text">Hello</h5>
                </div>
              </li>
              <li className="cards__item">
                <figure
                  className="cards__item__pic-wrap"
                  data-category="Mercedes"
                >
                  <img
                    className="cards__item__img"
                    alt="img"
                    src="https://carloson.ru/uploads/images/cars/62/5517804b683b93f62d6c03612223a1bd-740x507.jpg"
                  />
                </figure>
                <div className="cards__item__info">
                  <h5 className="cards__item__text">Hello</h5>
                </div>
              </li>
              <li className="cards__item">
                <figure
                  className="cards__item__pic-wrap"
                  data-category="Mercedes"
                >
                  <img
                    className="cards__item__img"
                    alt="img"
                    src="https://carloson.ru/uploads/images/cars/62/5517804b683b93f62d6c03612223a1bd-740x507.jpg"
                  />
                </figure>
                <div className="cards__item__info">
                  <h5 className="cards__item__text">Hello</h5>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </>
  );
};

export default LandingPage;
