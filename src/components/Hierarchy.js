import React, { Component } from 'react'
import { Card, CardTitle, CardText, Icon } from 'react-mdl'
import { repeat } from 'lodash'

export default class Hierarchy extends Component {
  componentWillMount() {
    this.props.relay.setVariables({
      tsn: parseInt(this.props.params.tsn),
      level: parseInt(this.props.params.level)
    })
  }

  getSpecies = (edge, iteration) => {
    return edge.node.children.edges.map(edge => {
      let row = null
      if (edge.node.children) {
        row = this.getSpecies(edge, iteration + 1)
      }

      const taxonomicUnit = edge.node.taxonomicUnit.edges[0].node
      const rankName = taxonomicUnit.taxonUnitType.edges[0].node.rankName.trim()

      return (
        <tr key={edge.node.id}>
          <td colSpan={4}>
            <table style={{width: '100%'}}>
              <tbody>
                <tr>
                  <td style={{width: '25%'}}>
                    {repeat('--', iteration)} {edge.node.tsn}
                  </td>
                  <td style={{width: '25%'}}>
                    {rankName}: {taxonomicUnit.completeName}
                  </td>
                  <td style={{width: '25%'}}>
                    {taxonomicUnit.credibilityRtng}
                  </td>
                  <td style={{width: '25%'}}>

                  </td>
                </tr>
                {row}
              </tbody>
            </table>
          </td>
        </tr>
      )
    })
  }

  render() {
    if (!this.props.viewer.hierarchies) {
      return <div>Loading...</div>
    }

    return (
      <Card style={{width:'100%'}}>
        <CardTitle>List for Kingdom Animalia</CardTitle>

        <CardText>
          <table style={{width: '100%'}}>
            <thead>
              <tr>
                <th style={{textAlign: 'left', width: '25%'}}>TSN</th>
                <th style={{textAlign: 'left', width: '25%'}}>Name</th>
                <th style={{textAlign: 'left', width: '25%'}}>Credibility Rating</th>
                <th style={{textAlign: 'left', width: '25%'}}>Synonym(s)</th>
              </tr>
            </thead>
            <tbody>
              {this.props.viewer.hierarchies.edges.map(edge => {
                const taxonomicUnit = edge.node.taxonomicUnit.edges[0].node
                const rankName = taxonomicUnit.taxonUnitType.edges[0].node.rankName.trim()

                return (
                  <tr key={edge.node.id}>
                    <td colSpan={4}>
                      <table style={{width: '100%'}}>
                        <tbody>
                          <tr>
                            <td style={{width: '25%'}}>
                              {edge.node.tsn}
                            </td>
                            <td style={{width: '25%'}}>
                              {rankName}: {taxonomicUnit.completeName}
                            </td>
                            <td style={{width: '25%'}}>
                              {taxonomicUnit.credibilityRtng}
                            </td>
                            <td style={{width: '25%'}}>

                            </td>
                          </tr>
                          {this.getSpecies(edge, 1)}
                        </tbody>
                      </table>
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </CardText>
      </Card>
    )
  }
}
