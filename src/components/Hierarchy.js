import React, { Component } from 'react'
import { Card, CardTitle, CardText, List, ListItem } from 'react-mdl'

export default class Hierarchy extends Component {
  render() {
    return (
      <Card>
        <CardTitle>List for Kingdom Animalia</CardTitle>

        <CardText>
          <List>
            {this.props.viewer.hierarchies.edges.map(edge => {
              return (
                <ListItem key={edge.node.id}>
                  {edge.node.taxonomicUnit.edges[0].node.completeName}
                  <List>
                    {edge.node.children.edges.map(edge => {
                      return <ListItem>{edge.node.taxonomicUnit.edges[0].node.completeName}</ListItem>
                    })}
                  </List>
                </ListItem>
              )
            })}
          </List>
        </CardText>
      </Card>
    )
  }
}
