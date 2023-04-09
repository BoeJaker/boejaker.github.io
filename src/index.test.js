import { fireEvent, getByText, getByTestId } from '@testing-library/dom'
import '@testing-library/jest-dom/extend-expect'
import { JSDOM } from 'jsdom'
import fs from 'fs'
import path from 'path'

const html = fs.readFileSync(path.resolve(__dirname, './index.html'), 'utf8');

let dom
let container

describe('index.html', () => {
  beforeEach(() => {
    // Constructing a new JSDOM with this option is the key
    // to getting the code in the script tag to execute.
    // This is indeed dangerous and should only be done with trusted content.
    // https://github.com/jsdom/jsdom#executing-scripts
    dom = new JSDOM(html, { runScripts: 'dangerously' })
    container = dom.window.document.body
  })

  it('contains a div with the id of welcome', () => {
    const welcomeDiv = container.querySelector('#welcome');
    expect(welcomeDiv).not.toBeNull();
  })
  it('contains a div with the id of about', () => {
    const welcomeDiv = container.querySelector('#about');
    expect(welcomeDiv).not.toBeNull();
  })
  it('contains a div with the id of layouts', () => {
    const welcomeDiv = container.querySelector('#layouts');
    expect(welcomeDiv).not.toBeNull();
  })
  it('contains a div with the id of elements', () => {
    const welcomeDiv = container.querySelector('#elements');
    expect(welcomeDiv).not.toBeNull();
  })
  it('contains a div with the id of contact', () => {
    const welcomeDiv = container.querySelector('#contact');
    expect(welcomeDiv).not.toBeNull();
  })
  it('renders the welcome banner', () => {
    const welcomeDiv = container.querySelector('#welcomebanner');
    expect(welcomeDiv).not.toBeNull();
  })
  it('fills the screen', () => {
    const content = container.querySelector('page');
    const { width, height } = content.getBoundingClientRect();

    expect(width).toBe(container.clientWidth);
    expect(height).toBe(container.clientHeight);
  });
  // it('renders a link element', () => {
  //   expect(getByText(container, 'tel:')).toHaveAttribute('href', 'tel:07761544030');
  // })
  ;
//   it('renders a button element', () => {
//     expect(container.querySelector('button')).not.toBeNull()
//     expect(getByText(container, 'Click me for a terrible pun')).toBeInTheDocument()
//   })

//   it('renders a new paragraph via JavaScript when the button is clicked', async () => {
//     const button = getByText(container, 'Click me for a terrible pun')
    
//     fireEvent.click(button)
//     let generatedParagraphs = container.querySelectorAll('#pun-container p')
//     expect(generatedParagraphs.length).toBe(1)

//     fireEvent.click(button)
//     generatedParagraphs = container.querySelectorAll('#pun-container p')
//     expect(generatedParagraphs.length).toBe(2)

//     fireEvent.click(button)
//     generatedParagraphs = container.querySelectorAll('#pun-container p')
//     expect(generatedParagraphs.length).toBe(3)
//   })
})