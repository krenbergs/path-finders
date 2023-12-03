import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const controls = new OrbitControls( camera, renderer.domElement );

function createCube(position, color, edgeColor) {
	const geometry = new THREE.BoxGeometry( 1, 1, 1 );
	const material = new THREE.MeshBasicMaterial( { color: color } );
	const cube = new THREE.Mesh( geometry, material );
	cube.position.set(position.x, position.y, position.z);
	scene.add( cube );

	// Create an edges geometry from the cube
	const edges = new THREE.EdgesGeometry( geometry );
	// Create a line segments object with the edges geometry and a line basic material
	const line = new THREE.LineSegments( edges, new THREE.LineBasicMaterial( { color: edgeColor } ) );
	// Add the line segments to the cube
	cube.add( line );
}

camera.position.z = 5;

function animate() {
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
}

export default function(coordinates, color, edgeColor) {
    coordinates.forEach(coord => {
        createCube(new THREE.Vector3(coord[0], coord[1], coord[2]), color, edgeColor);
    });
    animate();
}
