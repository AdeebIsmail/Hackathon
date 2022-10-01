import homebg from "../hiker.svg";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import "../fonts.css";
import Button from "react-bootstrap/Button";
import Dropdown from "react-bootstrap/Dropdown";
import React, { useState, useRef } from "react";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import Form from "react-bootstrap/Form";

function Home(props) {
  const [firstlocation, setFirstLocation] = useState("");
  const [secondlocation, setSecondLocation] = useState("");

  const setData = (e) => {
    e.preventDefault();
    console.log(firstlocation);
  };
  return (
    <div style={{ height: "100vh" }}>
      <div
        style={{
          backgroundImage: `url(${homebg})`,
          backgroundPosition: "center",
          backgroundSize: "cover",
          backgroundRepeat: "no-repeat",
          width: "100vw",
          height: "100vh",
        }}
      >
        <div
          style={{
            position: "absolute",
            top: "20%",
            left: "50%",
            transform: "translate(-50%, -50%)",
          }}
        >
          <Form onSubmit={setData}>
            <Row>
              <Col xs lg="2"></Col>
              <Col style={{ marginBlock: "1em", fontSize: "3vh" }} md="auto">
                Welcome to TravelHelper{" "}
              </Col>
              <Col xs lg="2"></Col>
            </Row>
            <Row>
              <Col>
                {" "}
                <Form.Select
                  aria-label="Default select example"
                  onChange={(text) => {
                    setFirstLocation(text.target.value);
                  }}
                >
                  <option>Starting Location</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </Form.Select>
              </Col>
              <Col>
                {" "}
                <Form.Select
                  aria-label="Default select example"
                  onChange={(text) => {
                    setSecondLocation(text.target.value);
                  }}
                >
                  <option>Ending Location</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </Form.Select>
              </Col>
            </Row>
          </Form>
        </div>
        <div
          style={{
            position: "absolute",
            top: "33%",
            left: "50%",
            transform: "translate(-50%, -50%)",
          }}
        >
          <Button variant="primary" onClick={(e) => setData(e)}>
            Submit
          </Button>
        </div>
      </div>
    </div>
  );
}

export default Home;
